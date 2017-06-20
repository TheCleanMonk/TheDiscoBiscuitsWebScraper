import urllib.request
import re

htmlfile = urllib.request.urlopen("http://unminify.com/")

htmltext = htmlfile.read()

pattern = re.compile(b'<div id="like-it">(.+?)</div>')

price = re.findall(pattern,htmltext)

print(price)