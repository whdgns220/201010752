import pymongo
from pymongo import MongoClient
client=MongoClient('localhost:27017')
db=client.Employees
db.mytable.insert({
        "name":"js"
    })

empCol=db.mytable.find()
type(empCol)
for emp in empCol:
    print emp

type(emp)
emp['name']

import os
KEY="4d43494948776864313137446c764b6f"
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'


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
url+=LINE_NUM

import requests
myurl='http://openapi.seoul.go.kr:8088/4d43494948776864313137446c764b6f/xml/SearchSTNBySubwayLineService/1/5/2/'
data=requests.get(myurl).text

print data


import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text


import lxml
import lxml.etree
import StringIO

import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text


import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key="4d43494948776864313137446c764b6f"
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'


_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1
