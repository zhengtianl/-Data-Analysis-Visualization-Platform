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
nltk.download("stopwords")
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

# text_list = []
# for i in doc_list:
#     text = i['text']
#     text_list.append(text)

# text_str = ' '.join(text_list)
# words = word_tokenize(text_str)
# words_no_punc = []

# for word in words:
#     if word.isalpha():
#         words_no_punc.append(word.lower())




# #list of stopwords
# stopwords_list = stopwords.words("english")
# clean_words = []
# #Iterate through the words_no_punc list and add non stopwords to the new clean_words list
# for word in words_no_punc:
#     if word not in stopwords_list:
#         clean_words.append(word)

# fdist = FreqDist(clean_words)

# clean_words_string = " ".join(clean_words)

# # #generating the wordcloud
# wordcloud = WordCloud(background_color="white").generate(clean_words_string)

# # #plot the wordcloud
# plt.figure(figsize = (12, 12))
# plt.imshow(wordcloud)

# # #to remove the axis value
# plt.axis("off")
# plt.show()

def word_cloud(doc_list):
    text_list = []
    for i in doc_list:
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
    wordcloud = WordCloud(background_color="white").generate(clean_words_string)
    plt.figure(figsize = (12, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    return plt
