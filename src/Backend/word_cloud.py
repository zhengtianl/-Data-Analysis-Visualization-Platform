##Reference:
##https://medium.com/@siglimumuni/natural-language-processing-in-python-exploring-word-frequencies-with-nltk-918f33c1e4c3


from nltk import word_tokenize
from nltk.probability import FreqDist
import urllib.request
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import couchdb
from nltk.corpus import stopwords
# nltk.download("stopwords")
import requests

server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')
db = server['twitter_huge_loc_tiny']


view_url = 'http://admin:admin@172.26.133.182:5984/twitter_huge_loc_tiny/_design/new/_view/idtextwithalcohol?reduce=false'
response = requests.get(view_url, auth=('admin', 'admin'))
data = response.json()
# 将文档转换为字典列表
doc_list = []
for row in data['rows']:
    doc_list.append(row)

def word_cloud(doc_list):
    text_list = []
    for i in doc_list:
        if 'value' in i:
            text = i['value']
            text_list.append(text)
    text_str = ' '.join(text_list)
    words = word_tokenize(text_str)
    words_no_punc = []
    for word in words:
        if word.isalpha():
            words_no_punc.append(word.lower())
    stopwords_list = stopwords.words("english")
    stopwords_list.extend(["https",'amp','one'])
    clean_words = []
    for word in words_no_punc:
        if word not in stopwords_list:
            clean_words.append(word)
    clean_words_string = " ".join(clean_words)
    
    return clean_words_string

print(type(word_cloud(doc_list)))