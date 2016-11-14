import json
import oauth2 as oauth

Consumer_Key = "dc0eZ3zFaOFFdkUoWmIVms72W"
Consumer_Secret = "qOQMweqA3GT0XqAyK9bWVTXS9TZJfHj78fBRvBVBzxqJRFmrNy"
Access_Token = "786057611166773249-WYglj3fxUPW23sOfBRJboVAiIF5gaAt"
Access_Token_Secret = "AZNzz8C2edrA85L0Mvg6WLKC0RUO6onKVyiVkcNe7BKti"

consumer = oauth.Consumer(key=Consumer_Key, secret=Consumer_Secret)
access_token = oauth.Token(key=Access_Token,secret=Access_Token_Secret)
client = oauth.Client(consumer,access_token)



import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello World'})
response,content=client.request(url,method='POST',body=mybody)



import io
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)









from pymongo import MongoClient
_mclient = MongoClient()
_db=_mclient.ds_twitter
_table=_db.home_timeline








url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, content = client.request(url)

home_timeline = json.loads(content)
for tweet in home_timeline:
    print content













url = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=2"
response, content = client.request(url)

home_timeline = json.loads(content)
for tweet in home_timeline:
    print tweet['id'],tweet['text']









print home_timeline[0]['created_at']
print home_timeline[0]['id']











import urllib
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
myparam={'max_id':'532386310086881280'}
mybody=urllib.urlencode(myparam)

response, content = client.request(url+"?"+mybody, method="GET")
home_timeline = json.loads(content)











import urllib
myparam={'max_id':'534949539757555713','since_id':'532386310086881280'}

mybody=urllib.urlencode(myparam)

response, content = client.request(url+"?"+mybody, method="GET")
home_timeline = json.loads(content)