
import urllib
response = urllib.urlopen('http://python.org/')
_html = response.read()
print response.info()
print len(_html)
print type(_html)

##regex

import re

p=re.compile('href="(http://.*?)"')
nodes=p.findall(_html)
print "http url은 몇 개?",len(nodes)
for node in nodes:
    print node

import re
p=re.compile('<h1>(.*?)</h1>')
h1tags=p.findall(_html)
for tag in h1tags:
    print tag

import re
p=re.compile('<p>(.*?)</p>')
ptags=p.findall(_html)

print len(ptags)

print ptags[0]


##BeautifulSoup


from bs4 import BeautifulSoup
tree=BeautifulSoup(_html, "lxml")
strongtags=tree('strong')
for tag in strongtags:
    print tag

from urllib import urlopen
from bs4 import BeautifulSoup
_html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
tree = BeautifulSoup(_html, "lxml")
for link in tree.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

