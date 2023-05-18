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
server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')  # 替换为实际的用户名和密码
db = server['twitter_huge_loc_tiny']
all_docs = db.view('_all_docs', include_docs=True)

# 将文档转换为字典列表
doc_list = []
for row in all_docs:
    doc = row['doc']
    doc_dict = dict(doc)
    doc_list.append(doc_dict)


def word_cloud(doc_list):
    text_list = []
    for i in doc_list:
        if 'text' in i:
            text = i['text']
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

