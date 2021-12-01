#!/usr/bin/env python
# coding: utf-8

# In[7]:
import pyspark, os, re
from pyspark import SparkContext, SparkConf
conf = SparkConf()
sc = SparkContext.getOrCreate(conf=conf)


# In[3]:
directory = '/notebooks/Data'
stop_words = ['they', 'she', 'he','it','the','as','is','and']
joined = None
for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename
        


# In[23]:
directory = '/notebooks/Data'
stop_words = ['they', 'she', 'he','it','the','as','is','and']
joined = None
for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename
        textFile = sc.textFile(filepath)
        # filter out stop word
        rdd = textFile.flatMap(lambda x: x.split()).filter(lambda x: x not in stop_words).persist()
        # remove punctuation
        rdd = rdd.map(lambda x : re.sub(r'[^\w\s]', '', x))
        # count frequency
        rdd = rdd.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)
        # map word to (filepath, frequency)
        path = "file:" + filepath
        rdd = rdd.map(lambda x : (x[0], (path, x[1])))
        if (joined == None):
            joined = rdd.persist()
        else:
            joined = joined.union(rdd).persist()


# In[31]:
# group by term 
grouped = joined.groupByKey().mapValues(list)
# save as textfile
grouped.saveAsTextFile("/notebooks/Data/output.txt")
