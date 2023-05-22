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
import requests
import json

with open('sentiment.json', 'r') as json_file:
    # Read the contents of the file
    json_data = json_file.read()
    # Parse the JSON data
    data = json.loads(json_data)


doc_list = []
for row in data['rows']:
     doc_list.append(row)



def word_cloud(doc_list):
    stopwords_list = set(stopwords.words("english"))
    stopwords_list.update(["https", 'amp', 'one'])

    text_list = [i['value']['text'] for i in doc_list if 'value' in i]
    text_str = ' '.join(text_list)

    words = word_tokenize(text_str)
    words_no_punc = (word.lower() for word in words if word.isalpha())

    clean_words = [word for word in words_no_punc if word not in stopwords_list]
    clean_words_string = " ".join(clean_words)
    
    return clean_words_string

# print(word_cloud(doc_list))