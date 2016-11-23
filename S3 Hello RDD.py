# 문제 S-3: Hello RDD


c=list([36.5,32,35,37.3,30])
def c2f(c):
    f=list()
    for x in c:
        _c=9./5*x+32;
        f.append(_c)
    return f


print c2f(c)


celsius = [39.2, 36.5, 37.3, 37.8]

def c2f(c):
    return (float(9)/5)*c + 32

f=map(c2f, celsius)
print f


map(lambda c:(float(9)/5)*c + 32, celsius)



## import os를 한 이후에 os.getwd()를 확인한 후에 확인할 것!!
   (밑에는 기본설정에 있는 data폴더에 저장한 거임)


%%writefile data/ds_spark_wiki.txt
Wikipedia
Apache Spark is an open source cluster computing framework.
아파치 스파크는 오픈 소스 클러스터 컴퓨팅 프레임워크이다.
Originally developed at the University of California, Berkeley's AMPLab,
the Spark codebase was later donated to the Apache Software Foundation,
which has maintained it since.
Spark provides an interface for programming entire clusters with
implicit data parallelism and fault-tolerance.


textFile=sc.textFile("data/ds_spark_wiki.txt")

type(textFile)

textFile.take(3)

textFile.first()

words=textFile.map(lambda x:x.split(' '))

words.collect()

textFile\
    .map(lambda x:len(x))\
    .collect()


## 바로 위에 \는 맵리듀스가 길 때 쓰는 거임!




_sparkLine=textFile.filter(lambda line:u"Spark" in line)

_sparkLine.count()


## 바로 위에 두 코딩은 저장된 것에서 "Spark"를 찾는 코딩


_sparkLine=textFile.filter(lambda line:u"스파크" in line)
_sparkLine.count()

## 바로 위에 두 코딩은 저장된 것에서 "스파크"를 찾는 것인데 그 앞에 u를 붙여야 함(한글)


a=[1,2,3]
myrdd=sc.parallelize(a)
myrdd.take(3)

squared=myrdd.map(lambda x:x*x)
squared.collect()

## 바로 위에 두 코딩을 통해 1,4,9가 나올꺼임


a=["this is a line","this is another line"]
myrdd=sc.parallelize(a)

words=myrdd.map(lambda x:x.split(' '))
words.collect()

## 바로 위에 코딩은 두 문장으로 나누는 코딩


myrdd\
    .map(lambda x:x.split(' '))\
    .collect()

## 바로 위에 코딩결과는 이거 바로 위에 결과와 같게 나옴


myrdd.map(lambda x:x.replace("a","AA")).collect()


## 바로 위에 코딩은 "a"를 "AA"로 바꾸는 코딩