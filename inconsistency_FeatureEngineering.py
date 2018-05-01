#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import csv
import re
import ast

soup = BeautifulSoup(open("PATH TO HTML FILE"), "html.parser")

list = [tag.name for tag in soup.find_all()]
tagset = set(list)
print (tagset)


countp = 0
pageStyle = soup.find('style').string
val=[]
#print(pageStyle[pageStyle.findall("{")+1:pageStyle.findall("}")])
defaultStyleList = re.findall('\{.*?\}',pageStyle)
tags = re.findall('(\S+)\s*{(?!/)',pageStyle)
final = {}
value= []
tempList = {}
print(type(defaultStyleList))
itera = 0

for i in defaultStyleList:
    i= str(i.replace(";", ","))
    i = i[1:-1]
    val =i.split(',')
    tempList ={}
    for j in val:
        if(j==' ' or j==''):
            val.remove(j)
    for j in val:
        key , dictval = j.split(':')
        key = key.strip()
        dictval = dictval.strip()
        tempList[key] = dictval
    final[tags[itera]] = tempList
    itera = itera +1




u1=0
lispp = []

dictp ={}
dictu1={}

textp={}

par = {}

for u in soup.find_all('u'):
    u1 = u1+1
    print(str(u.get('style')) + 'u')
    print(str(u1)+ 'u')
    tagu = 'u' + str(u.get('style'))
    if(u.get('style')!= None):
        str1 = u.get('style')
        str1 = str1.replace(";", ",")
        underl = str1.split(',')
        un = {}
        for j in underl:
            if(j==' ' or j==''):
                underl.remove(j)
        for i in underl:
            key, vals = i.split(':')
            un[key] = val
        dictu1[tagu] = un
for para in soup.find_all('p'):
    countp= countp+1
    temp = {}
    tagp = 'p' + str(countp) 
    if(para.get('style')!= None):
        str1 = para.get('style')
        str1= str1.replace(";", ",")
        para = str1.split(',')
        par ={}
        for j in para:
            if(j==' ' or j==''):
                para.remove(j)
        for i in para:
            key, vals  = i.split(':')
            par[key] = vals  
        dictp[tagp] = par
        temp = para.getText()
        textp[tagp]= temp

print(textp)
finalkey = []
finalval = []
for k in final['P']:
        finalkey.append(k)
        finalval.append(final['P'][k])

print(finalkey)
print(finalval)
incost = []

keyOFp = []
valuesOFp=[]
for i in dictp:
    keyOFp=[]
    valuesOFp=[]
    for j in dictp[i]:
        keyOFp.append(j)
        valuesOFp.append(dictp[i][j])
    print('\n')
    for p in keyOFp: 
        p = p.strip()
        print(p)
        insk = 0
        insv = 0
        for q in finalkey:
            if(p!=q):
                insk = insk+1
                print(p)
                print(q)
            if(p==q):
                dictp[i][p] = dictp[i][p].strip()
                if(dictp[i][p] != final['P'][q]):
                    incost.append(i)
                    break
        if(insk==3):
            incost.append(i)
            break


print(incost)
for i in incost:
    print(textp[i].strip())