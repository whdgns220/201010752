T-3: Twitter에 'Seoul'을 2015년 12월 한 달 분량을 읽는다.



import json
import oauth2 as oauth

Consumer_Key = "dc0eZ3zFaOFFdkUoWmIVms72W"
Consumer_Secret = "qOQMweqA3GT0XqAyK9bWVTXS9TZJfHj78fBRvBVBzxqJRFmrNy"
Access_Token = "786057611166773249-WYglj3fxUPW23sOfBRJboVAiIF5gaAt"
Access_Token_Secret = "AZNzz8C2edrA85L0Mvg6WLKC0RUO6onKVyiVkcNe7BKti"

consumer = oauth.Consumer(key=Consumer_Key, secret=Consumer_Secret)
access_token = oauth.Token(key=Access_Token,secret=Access_Token_Secret)
client = oauth.Client(consumer,access_token)



# since_id 또는 max_id를 써야 함.


import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':200,'since_id':'795321575440601088'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)





tsearch_json['statuses'][-1]['id'] --> 맨 마지막에서 -1 뺀거





print len(tsearch_json)
print len(tsearch_json['statuses'])





for tweet in tsearch_json['statuses']:
    print tweet['id']






f=open('ds_twitter_3.txt','w')
for j,tweet in enumerate(tsearch_json['statuses']):
    print i,tweet['id'],tweet['text']
    j=json.dumps([j,tweet['id'],tweet['text']])
    f.write(j)
f.close()







prev_id=None
f=open('_todel3.txt','a')
for i in range(0,20):
    myparam={'q':'seoul','count':10,'max_id':prev_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json['statuses'])
    for i,tweet in enumerate(tsearch_json['statuses']):
        #print str(i),tweet['id'],tweet['user']['name'],tweet['text']
        f.write(json.dumps([str(i),tweet['id'],tweet['user']['name']]))
        f.write("\n")
    #if data["statuses"] == []:
    #    print "end of data"
    #    break
    #else:
    prev_id=int(tsearch_json['statuses'][-1]['id'])-1
    print prev_id
f.close()









