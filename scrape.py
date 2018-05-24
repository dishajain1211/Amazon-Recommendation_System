from bs4 import BeautifulSoup
import urllib2
import requests
import os
base = "https://www.gutenberg.org/browse/scores/top#authors-last1/"
core = "https://www.gutenberg.org"
http = "https:"
res = requests.get(base)
urls= []
final = []
soup = BeautifulSoup(res.text, 'xml')

list1 = soup.find('ol')
for i in list1.find_all('a', href = True):
    urls.append(i['href'])

print(urls)
    
for link  in urls:
    target = core +link
    qwe = requests.get(target)
    chop = BeautifulSoup(qwe.text, 'xml')
    for i in chop.find_all('a', href= True):
        if(i.get_text() == 'Read this book online: HTML'):
            temp = http + i['href']
            final.append(temp)
            print(temp)


path = "/Users/ayushi/Desktop/dataset"
i=0
for links in final:
    url = links
    response = urllib2.urlopen(url)
    webContent = response.read()
    completeName = os.path.join(path, str(i) +".html")         
    f = open( completeName , 'w')
    f.write(webContent)
    f.close
    i=i+1