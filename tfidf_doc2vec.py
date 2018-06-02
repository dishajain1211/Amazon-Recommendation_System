#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 

import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import math
import gensim
from gensim.models.doc2vec import TaggedDocument
from sklearn.metrics.pairwise import cosine_similarity
import re
import math
from collections import Counter
import numpy as np
import math
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import numpy
from sklearn.cluster import DBSCAN
from sklearn.decomposition import TruncatedSVD
import itertools
import numpy as np
import matplotlib.pyplot as plt
from dbscan import GenerateData as gd   

## TS-SS
def Cosine(vec1, vec2) :
    result = InnerProduct(vec1,vec2) / (VectorSize(vec1) * VectorSize(vec2))
    return result
    
def VectorSize(vec) :
    return math.sqrt(sum(math.pow(v,2) for v in vec))

def InnerProduct(vec1, vec2) :
    return sum(v1*v2 for v1,v2 in zip(vec1,vec2))

def Euclidean(vec1, vec2) :
    return math.sqrt(sum(math.pow((v1-v2),2) for v1,v2 in zip(vec1, vec2)))

def Theta(vec1, vec2) :
    return math.acos(Cosine(vec1,vec2)) + 10

def Triangle(vec1, vec2) :
    theta = math.radians(Theta(vec1,vec2))
    return (VectorSize(vec1) * VectorSize(vec2) * math.sin(theta)) / 2

def Magnitude_Difference(vec1, vec2) :
    return abs(VectorSize(vec1) - VectorSize(vec2))

def Sector(vec1, vec2) :
    ED = Euclidean(vec1, vec2)
    MD = Magnitude_Difference(vec1, vec2)
    theta = Theta(vec1, vec2)
    return math.pi * math.pow((ED+MD),2) * theta/360

def TS_SS(vec1, vec2) :
    return Triangle(vec1, vec2) * Sector(vec1, vec2)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def preprocessing(raw):
    wordlist = nltk.word_tokenize(raw)
    text = [w.lower() for w in wordlist if w not in stopwords_en]
    return text

stopwords_en = stopwords.words("english")

f1 = open('text1.txt', 'r', encoding = "utf8")
text1 = preprocessing(f1.read())

f2 = open('text2.txt', 'r', encoding = "utf8")
text2 = preprocessing(f2.read())

### freq dist calculation ###
wordset = set(text1).union(set(text2))
freqd_text1 = FreqDist(text1)
text1_count_dict = dict.fromkeys(wordset, 0)
for word in text1:
    text1_count_dict[word] = freqd_text1[word]

freqd_text2 = FreqDist(text1)
text2_count_dict = dict.fromkeys(wordset, 0)
for word in text2:
    text2_count_dict[word] = freqd_text2[word]


## tf calculation
freqd_text1 = FreqDist(text1)
text1_length  = len(text1)
text1_tf_dict = dict.fromkeys(wordset, 0)
for word in text1:
    text1_tf_dict[word] = freqd_text1[word] / text1_length

freqd_text2 = FreqDist(text2)
text2_length  = len(text2)
text2_tf_dict = dict.fromkeys(wordset, 0)
for word in text2:
    text2_tf_dict[word] = freqd_text2[word] / text2_length

## IDF calculation
text12_idf_dict = dict.fromkeys(wordset, 0)
text12_length = 2
for word in text12_idf_dict.keys():
    if word in text1:
        text12_idf_dict[word] += 1
    if word in text2:
        text12_idf_dict[word] += 1

for word, val in text12_idf_dict.items():
    text12_idf_dict[word] =  1 + math.log(text12_length / (float(val)))


## TF-IDF calculation
text1_tfidf_dict = dict.fromkeys(wordset, 0)
for word in text1:
    text1_tfidf_dict[word] = (text1_tf_dict[word]) * (text12_idf_dict[word])

text2_tfidf_dict = dict.fromkeys(wordset, 0)
for word in text2:
    text2_tfidf_dict[word] = (text2_tf_dict[word]) * (text12_idf_dict[word])

## List of tf-idf values for each doc
v1 = list(text1_tfidf_dict.values())
v2 = list(text2_tfidf_dict.values())
v3 = [v1, v2]


## Similarity score 
value = TS_SS(v1,v2)
print(sigmoid(value))

## Clustering using Dbscan
distance = gd(v3)
print(distance)

## print distances closer to clients doc
## TS-SS is another approach to get similarity score


## DOC2VEC
taggeddocs = []
doc1 = TaggedDocument(words = text1,  tags =[u'NEWS_1'])
text1_tag = taggeddocs.append(doc1)

doc2 = TaggedDocument(words = text2,  tags =[u'NEWS_2'])
text2_tag = taggeddocs.append(doc2)
print('\n')

## BUILD THE MODEL
model = gensim.models.Doc2Vec(taggeddocs, dm = 0 , alpha = 0.025 , size = 20 , min_alpha = 0.025, min_count = 0)

## TRAINING OF MODEL
model.train(taggeddocs, total_examples=model.corpus_count, epochs=model.epochs)
model.alpha -= 0.002
model.min_alpha= model.alpha



## Similarity score with respect to other docs new_sentence
new_sentence = "YOU don't know about me without you have read a book by the name of The Adventures of Tom Sawyer".split(" ")    
print('doc2vec similarity' + str(model.docvecs.most_similar(positive=[model.infer_vector(new_sentence)],topn=5)))
#print(model.docvecs[0])

## Clustering using Dbscan
x=[]
for i in range(2):
    X = x.append(model.docvecs[i])
distance1 = gd(x)
print(distance1)

## print distances closer to clients doc



