#sentiment detection main code#

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import VarianceThreshold
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier



#calculte time for KNN#
starttime = time.time()

#changing n_neighbors will bring different accuracy#
knn = KNeighborsClassifier(n_neighbors=20)

#predict label for new_X_test#
y_pred = knn.fit(new_X_train, new_Y_train).predict(new_X_test)
totaltime = time.time() - starttime

train_data = pd.read_csv("Train.csv", sep=',')
test_data = pd.read_csv("Test.csv", sep=',')

#separating instance and label for Train
X_train_raw = [x[0] for x in train_data[['text']].values]
Y_train = [x[0] for x in train_data[['sentiment']].values]

#separating instance and label for Test
X_test_raw = [x[0] for x in test_data[['text']].values]




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

import numpy as np
from sklearn.model_selection import train_test_split
# split train data into new train data and new predicted data
new_X_train, new_X_test, new_Y_train, new_Y_test = train_test_split(x_train_vt, Y_train, test_size = 0.2797, shuffle = False)



knn = KNeighborsClassifier(n_neighbors=20)

#predict label for new_X_test#
y_pred = knn.fit(new_X_train, new_Y_train).predict(new_X_test)




# if __name__ == "__main__":
#     meta_file = "meta_data.json"

#     with open("data_file.json") as file:
#         files = json.load(file)
#     for f in files:
#         parse_data(f, meta_file)

