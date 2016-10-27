import os
KEY="4d43494948776864313137446c764b6f"
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'
#params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)


"/xml/SearchSTNBySubwayLineService/1/5/1/"

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
print url

import requests
data=requests.get(myurl)

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

print data.text

myurl='http://openapi.seoul.go.kr:8088/4d43494948776864313137446c764b6f/xml/SearchSTNBySubwayLineService/1/5/1/'

r=requests.get("http://httpbin.org/get")

r.status_code

r=requests.get('http://httpbin.org/status.404')

r.status_code

r.headers

!curl https://httpbin.org/get


한글


r=requests.get("http://httpbin.org/encoding/utf8")

r.text

import locale

locale.getdefaultlocale()

teststr=r.text[:500]

print teststr