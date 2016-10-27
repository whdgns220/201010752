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
myurl='http://openapi.seoul.go.kr:8088/4d43494948776864313137446c764b6f/xml/SearchSTNBySubwayLineService/1/5/1/'
data=requests.get(myurl)

print data.text
f=open('p1.txt','w')
f.write(data)
f.close()
