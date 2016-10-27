import os
KEY="4d43494948776864313137446c764b6f"
TYPE='json'
SERVICE='CardSubwayStatisticsService'
START_INDEX='1'
END_INDEX='10'
USE_MON='6'


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
url+=USE_MON

import requests
myurl='http://openapi.seoul.go.kr:8088/4d43494948776864313137446c764b6f/xml/CardSubwayStatisticsService/1/5/201306/'
data=requests.get(myurl).text

print data

import re
p=re.compile('<RIDE_PASGR_NUM>(.+?)</RIDE_PASGR_NUM>') 
res=p.findall(data)
for item in res:
    print item

import re
p=re.compile('<ALIGHT_PASGR_NUM>(.+?)</ALIGHT_PASGR_NUM>') 
res=p.findall(data)
for item in res:
    print item