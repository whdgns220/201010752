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





## 문제 S-7: Kolmogorov-Smirnov 검증


from pyspark.mllib.stat import Statistics

parallelData = sc.parallelize([1.0, 2.0, 5.0, 4.0, 3.0, 3.3, 5.5])

# run a KS test for the sample versus a standard normal distribution
testResult = Statistics.kolmogorovSmirnovTest(parallelData, "norm", 0, 1)
print(testResult)


