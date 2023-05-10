import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.neighbors import KNeighborsClassifier
import collections
import matplotlib.pyplot as plt
import json

train_data = pd.read_csv("./Train.csv", sep=',')
test_data = pd.read_csv("Test.csv", sep=',')

with open('./twitter-data-small.json', 'r', encoding='utf-8') as data_file:
    id_data = json.load(data_file)

def model(train_data, id_data):
    #separating instance and label for Train
    X_train_raw = [x[0] for x in train_data[['text']].values]
    Y_train = [x[0] for x in train_data[['sentiment']].values]
    X_test_raw = []
    for i in id_data:
        # for j in region:
        #     if i['includes']['places'][0]['full_name'] == j:
        X_test_raw.append(i['data']['text'])
    #Adjustment for BoW(change ngram_range)#
    BoW_vectorizer_2 = CountVectorizer(analyzer = 'word',ngram_range =(1,2))
    #Build the feature set (vocabulary) and vectorise the Tarin dataset using BoW
    X_train_BoW_2 = BoW_vectorizer_2.fit_transform(X_train_raw)

    #Use the feature set (vocabulary) from Train to vectorise the Test dataset 
    X_test_BoW_2 = BoW_vectorizer_2.transform(X_test_raw)

    #set variance Threshold =0.0001#
    selector =VarianceThreshold(threshold=0.0001)
    #Using BoW#
    x_train_vt = selector.fit_transform(X_train_BoW_2)
    x_test_vt =selector.transform(X_test_BoW_2)

    new_X_train, new_X_test, new_Y_train, new_Y_test = train_test_split(x_train_vt, Y_train, test_size = 0.2797, shuffle = False)

    #changing n_neighbors will bring different accuracy#
    knn = KNeighborsClassifier(n_neighbors=20)

    #predict label for new_X_test#
    y_pred = knn.fit(new_X_train, new_Y_train).predict(new_X_test)
    result_df = pd.DataFrame(y_pred)
    #negative_count = result_df.count('negative')
    count = dict(collections.Counter(y_pred))
    return count

print(model(train_data, id_data))