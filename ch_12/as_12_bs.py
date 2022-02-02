import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1:
    url = ' http://py4e-data.dr-chuck.net/known_by_Eabha.html'

count = input('Enter Counts: ')
if len(count) < 1:
    count = 7
count = int(count)

position = input('Enter Position: ')
if len(position) < 1:
    position = 18
position = int(position)

while count > 1:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    pos = 0
    tags = soup('a')
    for tag in tags:
        pos += 1
        if pos == position:
            url = tag.get('href', None)
            # print(url)
            pos = 0
            break
    count -= 1

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')

pos = 0
for tag in tags:
    pos += 1
    if pos == position:
        print(tag.contents[0])
        break
