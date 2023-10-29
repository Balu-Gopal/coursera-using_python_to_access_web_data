import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())

info = json.loads(data)
sum =0

for counts in info['comments']:
    sum = sum + int(counts['count'])

print(sum)