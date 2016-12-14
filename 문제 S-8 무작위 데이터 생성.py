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





## 문제 S-8: 무작위 데이터 생성

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)


from pyspark.sql.functions import rand, randn
# Create a DataFrame with one int column and 10 rows.
df = sqlCtx.range(0, 10)
df.show()



df.select("id", rand(seed=10).alias("uniform"), randn(seed=27).alias("normal")).show()
df.describe().show()


df = sqlCtx.range(0, 10).withColumn('rand1', rand(seed=10)).withColumn('rand2', rand(seed=27))
print df.stat.corr('rand1', 'rand2')
print df.stat.corr('id', 'id')


names = ["Alice", "Bob", "Mike"]
items = ["milk", "bread", "butter", "apples", "oranges"]
df = sqlCtx.createDataFrame([(names[i % 3], items[i % 5]) for i in range(100)], ["name", "item"])
df.show(10)


df = sqlCtx.createDataFrame([(1, 2, 3) if i % 2 == 0 else (i, 2 * i, i % 4) for i in range(100)], ["a", "b", "c"])
print df.show(10)
freq = df.stat.freqItems(["a", "b", "c"], 0.4)