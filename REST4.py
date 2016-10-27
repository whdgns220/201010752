import os
KEY="4d43494948776864313137446c764b6f"
TYPE='json'
SERVICE='ListLocaldata470401S'
START_INDEX='1'
END_INDEX='10'


url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'

import requests
myurl='http://openapi.seoul.go.kr:8088/4d43494948776864313137446c764b6f/xml/ListLocaldata470401S/1/319/'
data=requests.get(myurl).text

print data

import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATMAN')
for node in nodes:
    print node.text