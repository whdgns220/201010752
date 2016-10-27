import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr

type(geostr)

import json
geojson=json.loads(geostr)

type(geojson)

print geojson['ip']

geojson.get('ip')

country=geojson.get('country_code')

print country.decode('utf-8')

import json
import urllib

def getCountry(ipAddress):
    response = urllib.urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("39.118.87.152"))

import requests
send_url = 'http://freegeoip.net/json/39.118.87.152'
r = requests.get(send_url)

j=json.loads(r.text)

type(j)

print j.keys()

print j['city']

for k,v in j.iteritems():
    print k,"\t: ",v