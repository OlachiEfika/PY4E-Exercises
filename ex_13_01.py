import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter location - ')
red = urllib.request.urlopen(url)

data = red.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
branch = tree.findall('.//count')

#print('Count:', counts)
count = []
for item in branch:
    count.append(int(item.text))
    
print('Count:', len(count))
print('Sum:', sum(count))