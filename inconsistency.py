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

for p in soup.body.find_all():
    if 'style' in p.attrs:
        print(p.attrs['style'])

for p in soup.body.find_all():
    if 'style' in p.attrs:
        print(p)

for p in soup.find_all('p'):
    if 'style' in p.attrs:
        del p.attrs['style']
