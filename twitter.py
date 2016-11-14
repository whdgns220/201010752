def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d




import os
os.path.expanduser("~")




import os

keyPath=os.path.join(os.getcwd(), 'src', 'twitter4j.properties')
key=getKey(keyPath)




import twitter

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client




_client.statuses.update(status="Hello Twitter 1 160777")





import oauth2 as oauth
import json
consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])



client = oauth.Client(consumer, token)



help(client.request)



import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello 21 160777'})
response,content=client.request(url,method='POST',body=mybody)



import io
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)



timeline = _client.statuses.home_timeline()




print type(timeline)
print len(timeline)


print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]



for tweet in timeline:
     print tweet['id'],tweet['text']