import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location - ')
red = urllib.request.urlopen(url)

data = red.read()
info = json.loads(data)

count = []
for item in info['comments']:
    count.append(int(item['count']))

print('Count:', len(count))
print('Sum:', sum(count))