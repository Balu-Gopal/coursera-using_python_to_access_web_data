import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter URL: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

sum = 0
counts = tree.findall("comments/comment/count")

for comment in counts:
    com = int(comment.text)
    sum = sum + com

print(sum)