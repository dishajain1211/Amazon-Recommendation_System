# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 01:04:20 2018

@author: Disha Jain
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("0.html"), "html.parser")

list = [tag.name for tag in soup.find_all()]
tagset = set(list)
print (tagset)

tagList = []

soup.select("style")
tag = soup.style
type(tag)
print(tag)
tag.contents

tagSplit = tag.contents[0].split('}')

AttributeList = []
mainAttributeList = []

for i in tagSplit[0:13]:
    f = i.split('{')
    attributeSplit = f[1].split(';')
    AttributeList.append(attributeSplit)
       
for j in AttributeList:
    for k in j:
        if k:
            if k[0] == ' ':
                mainAttributeList.append(k[1:])
            elif k[1] == ' ':
                mainAttributeList.append(k[2:])
            else:
                mainAttributeList.append(k)
            
for p in soup.body.find_all():
    if 'style' in p.attrs:
        tempSplit = p.attrs['style'].split(';')
        for j in tempSplit:
            if j:
                if j[0] == ' ':
                    j = j[1:]
                if j not in mainAttributeList:
                    print(j)
            

#for p in soup.body.find_all():
#    if 'style' in p.attrs:
#        print(p)
#
#for p in soup.find_all('p'):
#    if 'style' in p.attrs:
#        del p.attrs['style']
