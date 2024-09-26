import xml.etree.ElementTree as ET


root = ET.Element('root')


filmovi = ET.SubElement(root, 'lista_filmova')
film = ET.SubElement(filmovi, 'film', naslov = 'Harry Potter and the Sorcerers Stone')
godina = ET.SubElement(film, 'godina')
zanr = ET.SubElement(film, 'zanr')

godina.text = '2001'
zanr.text = 'Avantura, Obiteljski, Fantazija'


film = ET.SubElement(filmovi, 'film', naslov = 'The Fall Guy')
godina = ET.SubElement(film, 'godina')
zanr = ET.SubElement(film, 'zanr')

godina.text = '2024'
zanr.text = 'Akcija, Komedija, Drama'


film = ET.SubElement(filmovi, 'film', naslov = 'The Gentleman')
godina = ET.SubElement(film, 'godina')
zanr = ET.SubElement(film, 'zanr')

godina.text = '2019'
zanr.text = 'Akcija, Kriminalistički'



tree = ET.ElementTree(root)
tree.write('lista_filmova.xml')


print(ET.tostring(root, encoding='utf8').decode('utf8'))
