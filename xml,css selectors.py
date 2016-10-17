%%writefile mypage.html
<!DOCTYPE html>
<html>
<head>
<title>My Home Page</title>
</head>
<body>
<h1>안녕하십니까</h1>
<p>오늘은 프로그래밍 하는 날...</p>
<p>Today we do programming...</p>
</body>
</html>

import webbrowser
import os

myuri='file://'+'localhost'+os.path.join(os.getcwd(), 'mypage.html')
webbrowser.open(myuri)


%%writefile mypage.html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>My Home Page</title>
</head>
<body>
<h1>안녕하십니까</h1>
<p>오늘은 프로그래밍 하는 날...</p>
<p>Today we do programming...</p>
</body>
</html>

webbrowser.open(myuri)

%%HTML
<!DOCTYPE html>
<html>
<head>
<title>My Home Page</title>
</head>
<body>
<h1>안녕하십니까</h1>
<p>오늘은 프로그래밍 하는 날...</p>
<p>Today we do programming...</p>
</body>
</html>

import webbrowser
myurl='https://www.google.co.kr/maps/place/Hongji-dong,+Jongno-gu,+Seoul/'
webbrowser.open(myurl)

import urllib
params = urllib.urlencode({"a": 4, "b": 20, "c": 2016, "d": 6, "e": 30, "f": 2016, "s": "^KS11"})
print params

%%HTML
<html>
<body>

<h2 class="my">Turn this into blue</h2>

<button onclick="myFunction()">Click</button>

<script>
function myFunction() {
    document.querySelector(".my").style.backgroundColor = "blue";
}
</script>

</body>
</html>

import webbrowser
myurl='https://www.google.co.kr/maps/place/Hongji-dong,+Jongno-gu,+Seoul/'
webbrowser.open(myurl)

import urllib
params = urllib.urlencode({"a": 4, "b": 20, "c": 2016, "d": 6, "e": 30, "f": 2016, "s": "^KS11"})
print params


##XML 파싱

import xml.etree.ElementTree as ET
tree=ET.parse('my.xml')
root=tree.getroot()
print root

for node in tree.getiterator():
    print node.tag, node.attrib

f=open('my.xml')
xmlstr=f.read()
f.close()

print type(xmlstr)

print xmlstr

import xml.etree.ElementTree as ET
tree=ET.fromstring(xmlstr)
for node in tree.getiterator():
    print node.tag, node.attrib

import lxml
import lxml.etree

tree=lxml.etree.parse('my.xml')
root=tree.getroot()

import StringIO
tree=lxml.etree.parse(StringIO.StringIO(xmlstr))

for node in tree.getiterator():
    print node.tag, node.attrib

nodes = tree.xpath("/wikimedia/projects/project/@name")
print len(nodes)

for node in nodes:
    print node

for node in nodes:
    print node

nodes = tree.xpath("/wikimedia/projects/project/editions/edition[@language='English']/text()")
print len(nodes)

for node in nodes:
    print node

nodes = tree.xpath("/wikimedia/projects/project[@name='Wikipedia']/editions/edition/text()")
print len(nodes)

for node in nodes:
    print node

##css selectors

%%HTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My Home Page</title>
    <style>
        h1 {text-align: center;
           color:red;
        };
    </style>
</head>
<body>
    <h1>안녕하십니까</h1>
    <p>오늘은 프로그래밍 하는 날...</p>
    <p>Today we do programming...</p>
</body>
</html>

type(tree)

