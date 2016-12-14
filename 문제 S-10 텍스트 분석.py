# coding: utf-8

# In[1]:

##문제 S-10: 텍스트 분석


# In[ ]:

#train 데이터 만들기


# In[ ]:


from pyspark.ml.feature import HashingTF, IDF, Tokenizer, RegexTokenizer
from pyspark.sql import SQLContext

sqlCtx = SQLContext(sc)
df = sqlCtx.createDataFrame(
    [
        [0,'my dog has flea problems. help please.'],
        [1,'maybe not take him to dog park stupid'],
        [0,'my dalmation is so cute. I love him'],
        [1,'stop posting stupid worthless garbage'],
        [0,'mr licks ate my steak how to stop him'],
        [1,'quit buying worthless dog food stupid'],
        [0,u'우리 강아지 벌레 있어요 도와주세요'],
        [0,u'우리 강아지 귀여워 너 사랑해'],
        [1,u'강아지 공원 가지마 바보같이'],
        [1,u'강아지 음식 구매 마세요 바보같이']
    ],
    ['cls','sent']
)


# In[ ]:

df.printSchema()


# In[ ]:

##tokenizer


# In[ ]:

tokenizer = Tokenizer(inputCol="sent", outputCol="words")


# In[ ]:

tokDf = tokenizer.transform(df)


# In[ ]:

for r in tokDf.select("cls", "sent").take(3):
    print(r)


# In[2]:

okDf.show()


# In[ ]:

#RegexTokenizer


# In[ ]:

e = RegexTokenizer(inputCol="sent", outputCol="wordsReg", pattern="\\s+")
regDf=re.transform(df)
regDf.show()


# In[ ]:

#Stop words


# In[ ]:


from pyspark.ml.feature import StopWordsRemover
stop = StopWordsRemover(inputCol="words", outputCol="nostops")


# In[ ]:

stopwords=list()

_stopwords=stop.getStopWords()
for e in _stopwords:
    stopwords.append(e)


# In[ ]:

_mystopwords=[u"나",u"너", u"우리"]
for e in _mystopwords:
    stopwords.append(e)


# In[ ]:

stopDf=stop.transform(tokDf)
stopDf.show()


# In[ ]:

#TF-IDF


# In[ ]:

from sklearn.feature_extraction.text import TfidfVectorizer

vocabulary = "a list of words I want to look for in the documents".split()
vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word', 
                 stop_words='english')
vect.fit(vocabulary)
tfidf=vect.transform(vocabulary)


# In[ ]:

hashTF = HashingTF(inputCol="words", outputCol="hash", numFeatures=50)
hashDf = hashTF.transform(tokDf)


# In[ ]:

hashDf.show()


# In[ ]:

#machine learning test


# In[ ]:


from pyspark.ml.classification import *

lr = LogisticRegression(maxIter=10, regParam=0.01)


# In[ ]:

from pyspark.ml.classification import DecisionTreeClassifier

dt = DecisionTreeClassifier(labelCol="label", featuresCol="features")
model=dt.fit(trainDf)


# In[3]:

from pyspark.mllib.regression import LabeledPoint
trainRdd = trainDf.map(lambda row: LabeledPoint(row.label,row.features))


# In[ ]:


from pyspark.mllib.classification import NaiveBayes

NaiveBayes.train(trainRdd)


# In[ ]:

from pyspark.mllib.regression import LinearRegressionWithSGD
LinearRegressionWithSGD.train(trainRdd)


# In[ ]:


from pyspark.mllib.classification import LogisticRegressionWithSGD
lrm = LogisticRegressionWithSGD.train(trainRdd, iterations=10)


# In[ ]:

from pyspark.mllib.classification import SVMWithSGD
svm = SVMWithSGD.train(trainRdd, iterations=10)