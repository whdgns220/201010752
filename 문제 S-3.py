import findspark

import os
os.getcwd()

import os
spark_home="C:/Users/DB400T2A/Downloads/spark-1.6.0-bin-hadoop2.6"

print spark_home

findspark.init(spark_home)

import pyspark

conf=pyspark.SparkConf()

conf=pyspark.SparkConf().setAppName("myApp")

sc=pyspark.SparkContext(conf=conf)

sc

sc.version

sc.master

sc._conf.getAll()




##문제 S-3: RDD를 사용하여 MLlib의 입력 데이터 word vector생성하기.


lines=sc.textFile("data/ds_spark_wiki.txt")
wc=lines.flatMap(lambda x:x.split())  ##flatmap은 통으로 함
wc.collect()


wc=lines.map(lambda x:x.split())  ##map은 라인별로 함
wc.collect()



## 라인 별 word count


from operator import add
wc = sc.textFile("data/ds_spark_wiki.txt")\
    .map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower())\
    .map(lambda x:x.split())\
    .map(lambda x:[(i,1) for i in x])

wc.collect()

for e in wc.collect():
    print e


##TF (Term Frequency)
##HashingTF


documents = sc.textFile("data/ds_spark_wiki.txt").map(lambda line: line.split(" "))

from pyspark.mllib.feature import HashingTF

hashingTF = HashingTF()
tf = hashingTF.transform(documents)

tf.collect()