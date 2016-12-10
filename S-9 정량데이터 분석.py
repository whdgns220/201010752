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





## S-9 정량데이터 분석


from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)




df = sqlCtx.createDataFrame(
    [
        ['No','young', 'false', 'false', 'fair'],
        ['No','young', 'false', 'false', 'good'],
        ['Yes','young', 'true', 'false', 'good'],
        ['Yes','young', 'true', 'true', 'fair'],
        ['No','young', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'good'],
        ['Yes','middle', 'true', 'true', 'good'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'good'],
        ['Yes','old', 'true', 'false', 'good'],
        ['Yes','old', 'true', 'false', 'excellent'],
        ['No','old', 'false', 'false', 'fair'],
    ],
    ['cls','age','f1','f2','f3']
)


df.printSchema()



from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(df)


df1=model.transform(df)


df1.printSchema()

df1.show()


labelIndexer = StringIndexer(inputCol="age", outputCol="att1")
model=labelIndexer.fit(df1)
df2=model.transform(df1)

labelIndexer = StringIndexer(inputCol="f1", outputCol="att2")
model=labelIndexer.fit(df2)
df3=model.transform(df2)

labelIndexer = StringIndexer(inputCol="f2", outputCol="att3")
model=labelIndexer.fit(df3)
df4=model.transform(df3)

labelIndexer = StringIndexer(inputCol="f3", outputCol="att4")
model=labelIndexer.fit(df4)
df5=model.transform(df4)

df5.printSchema()

df5.show()


from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

va = VectorAssembler(inputCols=["att1","att2","att3","att4"],outputCol="features")
df6 = va.transform(df5)


df7=df6.withColumnRenamed('labels','label')

df7.printSchema()


trainDf=df7.select('label','features')

trainDf.printSchema()

trainDf.show()




##RDD LabelPoint는 df에서 컬럼을 선택해서 만든다.


from pyspark.mllib.regression import LabeledPoint
trainRdd = trainDf.map(lambda row: LabeledPoint(row.label,row.features))


trainRdd.first()


##machine learning test


from pyspark.ml.classification import LogisticRegression
lr = LogisticRegression(maxIter=10, regParam=0.01)
model1 = lr.fit(trainDf)
print model1.coefficients
print model1.intercept


from pyspark.sql import Row
test0 = sc.parallelize([Row(features=Vectors.dense(2,0,0,1))]).toDF()
result = model1.transform(test0).head()


result.prediction