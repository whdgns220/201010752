웹데이터-4 : 한국 포털사이트에서 노래제목을 검색¶

##regex

import urllib
keyword='비오는'
f = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
mydata = f.read();


pos = mydata.find("트랙 리스트")
if (pos>0):
    pos = mydata.find("_title title NPI=", pos);
    pos = mydata.find("title=",pos+20)
    pos2 = mydata.find("\"", pos+8)
    print "---",mydata[pos+7:pos2]
print len(mydata)

import re
p=re.compile('title=".*비.?오는.*"')
#res=p.search(data)
res=p.findall(mydata)
for item in res:
    print item

##css selector

import lxml.html
import requests

keyword='비오는'
r = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")

_html = lxml.html.fromstring(r.text)

len(lxml.html.tostring(_html))

from lxml.cssselect import CSSSelector

sel = CSSSelector('table[summary] > tbody > ._tracklist_move > .name > a.title')
nodes = sel(_html)
len(nodes)

for node in nodes:
	  print node.text_content()

곡명, 아티스트, 앨범 모두 가져오기

from lxml.cssselect import CSSSelector

sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
nodes = sel(_html)
print lxml.html.tostring(nodes[0])

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
_name=_selName(nodes[1])
_artist=_selArtist(nodes[1])
_album=_selAlbum(nodes[1])

print _name[0].text_content()
print _artist[0].text_content().strip()
print _album[0].text_content()

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
for node in nodes:
	 _name=_selName(node)
    _artist=_selArtist(node)
    _album=_selAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
        print _album[0].text_content()