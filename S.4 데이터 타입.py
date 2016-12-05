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



## S.4 데이터 타입

from pyspark.mllib.linalg import Vectors
dv1=Vectors.dense([1,2,3])
print dv1

import numpy as np
dv2=np.array([1,2,3])
Vectors.dense(dv2)
Vectors.sparse(3,[1,2],[1.0,3.0])
sv1=Vectors.sparse(3,[1,2],[1.0,3.0])
sv1.toArray()



from pyspark.mllib.regression import LabeledPoint
LabeledPoint(1.0,Vectors.dense([1.0,2.0,3.0]))


from pyspark.sql import SQLContext


sqlCtx=SQLContext(sc)


trainDf=sqlCtx.createDataFrame([
        (1.0,Vectors.dense([0.0,1.1,0.1])),
        (1.0,Vectors.dense([0.0,1.1,0.1])),
         (1.0,Vectors.dense([0.0,1.1,0.1]))
    ],['label','features'])


trainDf.show()

trainDf.printSchema()


##labeld point(11/30)

from pyspark.mllib.regression import LabeledPoint


from pyspark.mllib.linalg import SparseVector, VectorUDT
from pyspark.sql.types import StructType, StructField, DoubleType
_rdd = sc.parallelize([
    (0.0, SparseVector(4, {1: 1.0, 3: 5.5})),
    (1.0, SparseVector(4, {0: -1.0, 2: 0.5}))])


schema = StructType([
    StructField("label", DoubleType(), True),
    StructField("features", VectorUDT(), True)
])


trainDf=_rdd.toDF(schema)
trainDf.printSchema()


## libsvm format

svmfn="C:\Users\DB400T2A\Downloads\spark-1.6.0-bin-hadoop2.6\data\mllib\sample_libsvm_data.txt"
svmDf=sqlCtx.read.format("libsvm").load(svmfn)

type(svmDf)
svmDf.printSchema()
svmDf.take(1)