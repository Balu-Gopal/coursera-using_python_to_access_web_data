import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url,context = ctx).read()
soup = BeautifulSoup(html,'html.parser')

sum = 0
count = 0
tags = soup('span')
for tag in tags:
    comment = tag.contents[0]
    sum = sum + int(comment)
    count = count + 1

print('Sum: ',sum)