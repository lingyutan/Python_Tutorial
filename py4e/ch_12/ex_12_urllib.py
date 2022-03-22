import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Look for code3/urllinks.py for SSL certificate errors

for line in fhand:
    print(line.decode().strip())
