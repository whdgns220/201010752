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





## S.6: DataFrame

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)


from pyspark.sql import Row
Person = Row('name', 'height')
rows = [Person('kim', 170), Person('lee', 175), Person('lim', 180),]
#rowsRdd = sc.parallelize(rows)
#rowsDf = sqlCtx.createDataFrame(rowsRdd)

rowsDF=sqlCtx.createDataFrame(rows)

type(rows)

type(rowsRdd)

type(rowsDF)

rowsDF.printSchema()

rowsDF.where(rowsDF.height < 175)\
    .select([rowsDF.name, rowsDF.height]).show()

rowsDF.groupby(rowsDF.height).max().show()