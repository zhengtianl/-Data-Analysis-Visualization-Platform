import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.neighbors import KNeighborsClassifier
import collections
# import matplotlib.pyplot as plt
import json
import couchdb
import requests
import csv
import itertools


with open('sentiment.json', 'r') as json_file:
    # Read the contents of the file
    json_data = json_file.read()
    # Parse the JSON data
    data = json.loads(json_data)

with open('mastodon.json', 'r') as json_file:
    # Read the contents of the file
    json_data = json_file.read()
    # Parse the JSON data
    data_mas = json.loads(json_data)

doc_list = []
for row in data['rows']:
     doc_list.append(row)

doc_list_mas = []
for row in data_mas['rows']:
     doc_list_mas.append(row)

unemploy_list = []
with open('unemploy.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dictionary = {
            "p_unemp_tot": int(row["p_unemp_tot"]),
            "lga_name16": str(row[" lga_name16"])
        }
        unemploy_list.append(dictionary)

for item in unemploy_list:
    city_name = item['lga_name16']
    start_index = city_name.find('(')
    if start_index != -1:
        city_name = city_name[:start_index].strip()
    item['lga_name16'] = city_name

train_data = pd.read_csv("Train.csv", sep=',')
test_data = pd.read_csv("Test.csv", sep=',')

def model(train_data, id_data):
    #separating instance and label for Train
    X_train_raw = [x[0] for x in train_data[['text']].values]
    Y_train = [x[0] for x in train_data[['sentiment']].values]
    X_test_raw = []
    for i in range(len(id_data) - 1):
        data = id_data[i]
        if 'value' in data:
            X_test_raw.append(data['value']['text'])
    #print(len(X_test_raw))
    BoW_vectorizer_2 = CountVectorizer(analyzer = 'word',ngram_range =(2,2))
    #Build the feature set (vocabulary) and vectorise the Tarin dataset using BoW
    X_train_BoW_2 = BoW_vectorizer_2.fit_transform(X_train_raw)
    #Use the feature set (vocabulary) from Train to vectorise the Test dataset 
    X_test_BoW_2 = BoW_vectorizer_2.transform(X_test_raw)
    #print(X_test_BoW_2)
    #print(X_test_BoW_2)
    #set variance Threshold =0.0001#
    selector =VarianceThreshold(threshold=0.0001)
    #Using BoW#
    # x_train_vt = selector.fit_transform(X_train_BoW_2)
    # x_test_vt =selector.transform(X_test_BoW_2)
    #new_X_train, new_X_test, new_Y_train, new_Y_test = train_test_split(x_train_vt, Y_train, test_size = 0.2797, shuffle = False)
    #print(new_X_test.shape)
    #changing n_neighbors will bring different accuracy#
    knn = KNeighborsClassifier(n_neighbors=5)

    #predict label for new_X_test#
    y_pred = knn.fit(X_train_BoW_2, Y_train).predict(X_test_BoW_2)
    result_df = pd.DataFrame(y_pred)
    #negative_count = result_df.count('negative')
    count = dict(collections.Counter(y_pred))
    return count

# print(model(train_data, doc_list_mas))