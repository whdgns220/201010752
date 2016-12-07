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




##문제 S-5: 파일에서 Spark SQL로 데이터 읽기



from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)




pDf=sqlCtx.read.json("C:/Users/DB400T2A/Downloads/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.json")

type(pDf)

pDf.show()

pDf.filter(pDf['age'] > 21).show()

pDf.registerTempTable("people") ## sql table 만들기

sqlCtx.sql("select name from people").show() 


##json frm url

import requests
r=requests.get("https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json")

wc=r.json()
type(wc)
print wc[0]


wcDf=sqlCtx.createDataFrame(wc)
wcDf.printSchema()


wcDf.registerTempTable("wc")
sqlCtx.sql("select Club,Team,Year from wc").show()