import nltk
import numpy as np
import pandas as pd 
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

WORD = re.compile(r"\w+")
my_punctuation = '!"$%&\'()*+,:;<=>?[\\]^_`{|}~•@#'   # left with / and - and .   
def Preprocessing3(text):
    text= re.sub("[\(\[].*?[\)\]]", "", text)                   # remove (..) [..]
    return text

# Specify url of the web page
source = urlopen('https://en.wikipedia.org/wiki/Hurricane_Sandy').read()
# Make a soup 
soup = BeautifulSoup(source,'lxml')
# Extract the plain text content from paragraphs
text = ''
for paragraph in soup.find_all('p'):
    text += paragraph.text
list1 = list(text.split(" ")) 
l=''
for i in range(len(list1)):
    l=l+' '+list1[i]
k=[]
k.append(l)
df= pd.DataFrame({'text':k})
df['text']=df['text'].apply(Preprocessing3)
d= df['text'][0].split('.')
dd=[]
for i in range(len(d)):
    ww=re.sub(r"^\s+", "", d[i], flags=re.UNICODE)
    w=ww.split('\n')
    if len(w)==1:
        dd.append(w[0])
    else:
        for j in range(len(w)):
            dd.append(w[j])
d_final=[]
for i in range(len(dd)):
    s=dd[i].split()
    if len(s)>3:
        d_final.append(dd[i])

df=pd.DataFrame({'text':d_final})
df.to_csv('Hurricane_Sandy.csv', index=False)






