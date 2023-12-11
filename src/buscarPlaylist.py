import xml.etree.ElementTree as ET
import os

Ruta = input('Coloca la ruta del XSPF= ')

rutaPlayList = os.path.join(Ruta)
tree = ET.parse(rutaPlayList)
root = tree.getroot()

def playlist():
    locations = []

    for child in root.findall('.//trackList/track/location'):
        location = child.text
        locations.append(location)

    return locations