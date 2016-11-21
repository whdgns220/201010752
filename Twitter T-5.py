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
url = "https://api.twitter.com/1.1/followers/list.json"

response, content = client.request(url, method="GET")
tfollower_json = json.loads(content)





print len(tfollower_json)
print type(tfollower_json)






for k,v in tfollower_json.iteritems():
    print k






for i in tfollower_json['users']:
    print i['id'],i['screen_name']