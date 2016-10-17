##한글

import locale
locale.getdefaultlocale()

import sys
print sys.getdefaultencoding()

print sys.stdin.encoding

print sys.stdout.encoding


str('한')

u'한'

print '한'

print u'한'


## 인터넷 한글 인코딩

import urllib

urllib.quote('/~jslm')

urllib.quote('%')


urllib.quote('#')


urllib.urlencode({'key':'%3D'})


##json(JavaScript Object Notation)



import json
In [31]:
input = '''[
    {"id":"001", "x":"2", "name":"Chuck"},
    {"id":"002", "x":"3", "name":"jsl"}
]'''

type(input)


Info=json.loads(input)

info0['id']

