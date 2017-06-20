import urllib.request
import re


urls = ["http://discobiscuits.net/setlists.php?year=2017"]
i=0

pattern = re.compile(b'<div class="setlist">(.+?)</div>')

while i<len(urls):
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern,htmltext)
    print(titles)
    i+=1