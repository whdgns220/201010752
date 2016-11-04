import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('https://www.ieee.org/conferences_events/index.html')

html = lxml.html.fromstring(r.text)


print lxml.html.tostring(html)


sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div:nth-child(2)')
nodes = sel(html)
for node in nodes:
    print lxml.html.tostring(node)


sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div a')
nodes = sel(html)
print nodes


for node in nodes:

    print node.text


sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div p > br')

nodes = sel(html)
print nodes

for node in nodes:
    print lxml.html.tostring(node)


sel=CSSSelector('div.box-c-indent p > a')
nodes = sel(html)
print len(nodes)
print nodes


for node in nodes:

    if node is not None:
        print node.text_content()


