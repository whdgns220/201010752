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