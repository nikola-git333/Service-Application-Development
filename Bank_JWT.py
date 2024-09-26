import sqlite3
import jwt
import datetime
from time import sleep


conn = sqlite3.connect('klijenti_banke.db')
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS klijenti(
 id INTEGER PRIMARY KEY AUTOINCREMENT, 
 ime_prezime TEXT NOT NULL,
 broj_racuna TEXT NOT NULL,
 lozinka TEXT NOT NULL,
 token TEXT)
 """)

conn.commit()


klijenti = [('Nikola Jerkan', '1234','45689'),
             ('Bojana Uskokovic','4321','78945'),
             ('Johnny Cage','5678','12345')]

for klijent in klijenti:
    cursor.execute('''INSERT INTO klijenti (ime_prezime, broj_racuna, lozinka) 
                 VALUES (?, ?, ?)''', klijent)
conn.commit()


cursor.execute('SELECT * FROM klijenti')
result = cursor.fetchall()
print('Klijenti :')
for el in result:
    print(el)
    

brojRacuna = input('\nUnesite broj računa:\n')
lozinka = input('Unesite lozinku:\n')


query = cursor.execute('SELECT %s FROM klijenti where %s=? and %s=?' 
 % ('ime_prezime', 'broj_racuna', 'lozinka'), (brojRacuna, lozinka,))


if (len(query.fetchall()) == 0):
    print('Neuspješna prijava, klijent ne postoji.')
else:
    kljuc = 'tajni_kljuc'
    token = jwt.encode({'racunKlijenta': brojRacuna,
                          'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=45)},
                         kljuc, algorithm='HS256')
    

    cursor.execute('UPDATE klijenti SET %s=? WHERE %s=? AND %s=?' % ('token','broj_racuna', 'lozinka'), 
                   (token, brojRacuna, lozinka,))
    conn.commit()
    
    print('\nDobrodošli vaša prijava je uspješna.')
    print('Vaš token vrijedi 45 sekundi:\n', token)


# funkcija za provjeru tokena    
'''
def provjera_tokena(token):
    try:
        decoded = jwt.decode(token, kljuc, algorithms=['HS256'])
        print('Dekodirani token:', decoded)
    except jwt.ExpiredSignatureError:
        print('Token je istekao.')
    except jwt.InvalidTokenError:
        print('Pogrešan token.')
        
sleep(30)
provjera_tokena(token)

# provjera nakon dodatnih 20 sekundi
sleep(20)
provjera_tokena(token) 
'''      


conn.close()