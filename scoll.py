import os
from bs4 import BeautifulSoup
import csv
import re
import ast
import pandas as pd
from pandas import DataFrame
import itertools
import numpy as np
directory = "/Users/ayushi/Desktop/amazon123/dataset"
count = 0
#for filename in os.listdir(directory):
#    if filename.endswith(".html"): 
#        print(os.path.join(directory, filename), count)
soup = BeautifulSoup(open("/Users/ayushi/Desktop/amazon123/dataset/2.html"), "html.parser")
page = soup.find('style').string
default = re.findall('\{.*?\}',page)
tags = re.findall('(\S+)\s*{(?!/)',page)
#print(default, "default")
#print(tags, "tags")

final = {}
value= []
listr=[]
x ={}
#print(type(default))
itera = 0
for i in default:
    i= str(i.replace(";", ","))
    i = i[1:-1]
    val =i.split(',')
    x ={}
    #print(val)
    for j in val:
        if(j==' ' or j==''):
            val.remove(j)
    #print(val)
    for j in val:
        key , dictval = j.split(':')
        key = key.strip()
        dictval = dictval.strip()
        x[key] = dictval
    final[tags[itera]] = x
    itera = itera +1
for k in list(final):
  if k.startswith('.'):
    final.pop(k)
s = set()
for dic in final:
   for val in final[dic]:
      s.add(val)
listofcolums= []
listofrow= []
for i in final:
    listofcolums.append(i)
for i in s:
    listofrow.append(i)

listofcolums = [i.split(',') for i in listofcolums]
listofcolums = list(itertools.chain.from_iterable(listofcolums))
print(listofcolums)
print(listofrow)
df = pd.DataFrame(columns= listofcolums, index=listofrow)
pis =[]
dictfinal = {}
for i,j in final.items():
    pis = i.split(',')
    print(pis)
    for values in pis:
        dictfinal[values] = j

#print(dictfinal)

for i in listofcolums:
        val=[]
        #print(i)
        for j in listofrow:
            try:
                #print(j)
                #print(final[i][j])
                val.append(dictfinal[i][j])
            except KeyError:
                val.append(np.nan)
                #print('error')
        df[i] = val


#print(df)
#df.replace(None,np.nan)
print(df)
df.to_csv("/Users/ayushi/Desktop/amazon123/csv/2.csv", sep=',')
#print(final)



count= count+1
