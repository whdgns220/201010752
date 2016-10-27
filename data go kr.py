import os
keyPath=os.path.join(os.getcwd(),'src','key.properties')
print keyPath

f=open(keyPath,'r')
lines=f.readlines()

d=dict()
d['a']=1
d['dataseoul']=1234
print d

for line in lines:
    row=line.split('=')
    d[row[0]]=row[1].strip()

print d

def getKey(Path):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines(): 
        row=line.split('=')
        d[row[0]]=row[1].strip()
    return d

import os
keyPath=os.path.join(os.getcwd(),'src','key.properties')
key=getKey(keyPath)

key['dataseoul']


SERVICE='ArpltnlnforlngireSvc'
OPERATION_NAME='getMinuDustFrcstDspth'
#param1=os.path.join(SERVICE,OPERATION_NAME)
param1=SERVICE+'/'+OPERATION_NAME
print param1

import urllib
d=dict()
d['dataTerm']='month'
param2=urllib.urlencode(d)
print param2


params=param1+'?'+'serviceKey='+key['gokr']+&'+param2
print params



import urlparse
url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
myurl=urlparse.urljoin(url,params)
print myurl