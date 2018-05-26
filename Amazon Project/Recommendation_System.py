# -*- coding: utf-8 -*-
"""
Created on Sat May 26 02:13:11 2018

@author: Disha Jain
"""
import math
import nltk
import codecs
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

file1 = codecs.open('Book1.html', 'r', 'utf8')
soup1 = BeautifulSoup(file1, 'html.parser')

file2 = codecs.open('Book2.html', 'r', 'utf8')
soup2 = BeautifulSoup(file2, 'html.parser')

tagList1 = [tag.name for tag in soup1.find_all()]
tagset1 = set()
for item in tagList1:
    tagset1.add(item)
    
tagList2 = [tag.name for tag in soup2.find_all()]
tagset2 = set()
for item in tagList2:
    tagset2.add(item)
    
words1 = []
words2 = []

stop_words = set(stopwords.words('english'))

for lines in soup1.body.get_text().split():
    if lines not in stop_words:
        words1.append(lines)
        
for lines in soup2.body.get_text().split():
    if lines not in stop_words:
        words2.append(lines)
    
fdist1 = nltk.FreqDist(words1)
print(fdist1.keys())

fdist2 = nltk.FreqDist(words2)
print(fdist2.keys())

tf1 = []
idf1 = []
weights1 = []

tf2 = []
idf2 = []
weights2 = []

tf_test = []
idf_test = []
weights_test = []

TextLength1 = len(words1)
print(TextLength1)

TextLength2 = len(words2)
print(TextLength2)

for i in fdist1.keys():
    current_tf = fdist1[i]/TextLength1
    tf1.append(current_tf)
    if i not in fdist2.keys():
        val = 2
        current_idf = math.log(val,) + 1
        idf1.append(current_idf)
    else:
        val = 1
        current_idf = math.log(val,) + 1
        idf1.append(current_idf)
    current_weight = current_tf * current_idf
    weights1.append(current_weight)

for i in fdist2.keys():
    current_tf = fdist1[i]/TextLength1
    tf2.append(current_tf)
    if i not in fdist1.keys():
        val = 2
        current_idf = math.log(val,) + 1
        idf2.append(current_idf)
    else:
        val = 1
        current_idf = math.log(val,) + 1
        idf2.append(current_idf)
    current_weight = current_tf * current_idf
    weights2.append(current_weight)

test = codecs.open('Test_book.html', 'r', 'utf8')
test_soup = BeautifulSoup(test, 'html.parser')

test_tagList = [tag.name for tag in test_soup.find_all()]
test_tagset = set()
for item in test_tagList:
    test_tagset.add(item)

test_words = []

for lines in test_soup.body.get_text().split():
    if lines not in stop_words:
        test_words.append(lines)

test_fdist = nltk.FreqDist(test_words)
print(test_fdist.keys())

tf_test = []
idf_test = []
weights_test = []

test_TextLength = len(test_words)
print(test_TextLength)

for i in test_fdist.keys():
    current_tf = test_fdist[i]/test_TextLength
    tf_test.append(current_tf)
    val = 1
    current_idf = math.log(val,) + 1
    idf_test.append(current_idf)
    current_weight = current_tf * current_idf
    weights_test.append(current_weight)

for i in range(9443 , 15534):
    weights2.append('0')

for i in range(13339 , 15534):
    weights1.append('0')
    
d = 0.0
den1 = 0.0
den2 = 0.0
for i in range(15534):
    d = d + (float(weights1[i]) * float(weights_test[i]))
    den1 = den1 + (float(weights1[i]) * float(weights1[i]))
    den2 = den2 + (float(weights_test[i]) * float(weights_test[i]))

den1 = math.sqrt(den1)
den2 = math.sqrt(den2)

costheta1 = d/(den1 * den2)
 
d = 0.0
den1 = 0.0
den2 = 0.0
for i in range(15534):
    d = d + (float(weights2[i]) * float(weights_test[i]))
    den1 = den1 + (float(weights2[i]) * float(weights2[i]))
    den2 = den2 + (float(weights_test[i]) * float(weights_test[i]))

den1 = math.sqrt(den1)
den2 = math.sqrt(den2)

costheta2 = d/(den1 * den2)  

print(costheta1)
print(costheta2)

if costheta1 > costheta2:
    print("test2.html book style is recommended")
else:
    print("test.html book stle is recommended")