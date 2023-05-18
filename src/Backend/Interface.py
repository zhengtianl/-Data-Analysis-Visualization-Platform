from flask import Flask, jsonify
import json
import pandas as pd
from flask_cors import CORS
from region_count import region_tweet_count, region
from sentiment_count import model
from alcohol import detect_alcohol
from Server import city_count
from word_cloud import word_cloud
import couchdb
app = Flask(__name__)
CORS(app)

server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')  
db = server['twitter_huge_loc_tiny']
all_docs = db.view('_all_docs', include_docs=True)
# 将文档转换为字典列表
doc_list = []
for row in all_docs:
    doc = row['doc']
    doc_dict = dict(doc)
    doc_list.append(doc_dict)




with open('twitter-data-small.json', 'r', encoding='utf-8') as data_file:
    id_data = json.load(data_file)

with open('Train.csv', 'r') as file:
    train_data = pd.read_csv(file, sep=',')

with open('Test.csv', 'r') as file:
    test_data = pd.read_csv(file, sep=',')

with open('sal.json', 'r', encoding='utf-8') as data_file:
    sal_data = json.load(data_file)

@app.route("/authorid", methods=["GET"])
def get_data_authorid():
    view = db.view('_design/new/_view/authorid', group=True)
    data = [row.value for row in view]
    return data



@app.route("/count", methods=["GET"])
def count():
    region_area = region(doc_list)
    tweet_count = region_tweet_count(doc_list, region_area)
    return jsonify({'region': region_area, 'count': tweet_count})

@app.route("/city_count", methods=["GET"])
def city_count_amount():
    city_count_dict = city_count(sal_data)
    return city_count_dict


@app.route("/alcohol", methods=["GET"])
def alcohol():
    region_area = region(doc_list)
    alcohol_count = detect_alcohol(doc_list, region_area)
    return jsonify({'region': region_area, 'alcohol_count': alcohol_count})


@app.route("/sentiment", methods=["GET"])
def sentiment():
    sentiment_list = model(train_data, doc_list)
    return jsonify({'sentiment_list': sentiment_list})

# @app.route("/wordcloud", methods=["GET"])
# def wordcloud():
#     cloud_figure = word_cloud(doc_list)
#     return jsonify({'image': cloud_figure})