from flask import Flask, jsonify, send_file
import json
import pandas as pd
from flask_cors import CORS
import couchdb
import requests

# from region_count import region_tweet_count, region
from sentiment_count import model
from alcohol import detect_alcohol,region
# from Server import city_count
from word_cloud import word_cloud


server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')
db = server['twitter_huge_loc_tiny']

app = Flask(__name__)
CORS(app)

with open('twitter-data-small.json', 'r', encoding='utf-8') as data_file:
    id_data = json.load(data_file)

with open('Train.csv', 'r') as file:
    train_data = pd.read_csv(file, sep=',')

with open('Test.csv', 'r') as file:
    test_data = pd.read_csv(file, sep=',')

with open('sal.json', 'r', encoding='utf-8') as data_file:
    sal_data = json.load(data_file)


@app.route("/alcohol_detect", methods=["GET"])
def get_data_alcohol():
    view_url = 'http://admin:admin@172.26.133.182:5984/twitter_huge_loc_large/_design/new/_view/keywords?group=true'
    response = requests.get(view_url, auth=('admin', 'admin'))
    data = response.json()
    doc_list = []
    for row in data['rows']:
        doc_list.append(row)

    region_list = region(doc_list)
    alcohol_count = detect_alcohol(doc_list, region_list)
    return jsonify({'region_alcohol_count': alcohol_count})


@app.route("/sentiment", methods=["GET"])
def sentiment():
    view_url = 'http://admin:admin@172.26.133.182:5984/twitter_huge_loc_tiny/_design/new/_view/idtextwithalcohol?reduce=false'
    response = requests.get(view_url, auth=('admin', 'admin'))
    data = response
    doc_list = []
    for row in data['rows']:
        doc_list.append(row)
    sentiment_detect = model(train_data, doc_list)
    totol_amount = len(doc_list)
    return jsonify({'sentiment_detect': sentiment_detect, 'total_amount':totol_amount})

@app.route("/wordcloud", methods=["GET"])
def wordcloud():
    view_url = 'http://admin:admin@172.26.133.182:5984/twitter_huge_loc_tiny/_design/new/_view/idtextwithalcohol?reduce=false'
    response = requests.get(view_url, auth=('admin', 'admin'))
    data = response
    doc_list = []
    for row in data['rows']:
        doc_list.append(row)
    clean_word_string = word_cloud(doc_list)
    return jsonify({'word_string': clean_word_string})





# @app.route("/authorid", methods=["GET"])
# def get_data_authorid():
#     TB = server['twitter_huge_loc_f']
#     view = TB.view('_design/new/_view/keywords', group=True)
#     data = [row.value for row in view]
#     return data


# @app.route("/keyword", methods=["GET"])
# def get_data_alcohol():
#     view = db.view('_design/new/_view/keywords', group=True)
#     data = [row.value for row in view]
#     return data

# @app.route("/count", methods=["GET"])
# def count():
#     region_area = region(doc_list)
#     tweet_count = region_tweet_count(doc_list, region_area)
#     return jsonify({'region': region_area, 'count': tweet_count})


# @app.route("/city_count", methods=["GET"])
# def city_count_amount():
#     city_count_dict = city_count(sal_data)
#     return city_count_dict


# @app.route("/alcohol", methods=["GET"])
# def alcohol():
#     region_area = region(doc_list)
#     alcohol_count = detect_alcohol(doc_list, region_area)
#     return jsonify({'region': region_area, 'alcohol_count': alcohol_count})


# @app.route("/sentiment", methods=["GET"])
# def sentiment():
#     sentiment_list = model(train_data, doc_list)
#     return jsonify({'sentiment_list': sentiment_list})


# @app.route("/wordcloud", methods=["GET"])
# def wordcloud():
#     cloud_figure = 'wordcloud.png'
#     return send_file(cloud_figure, mimetype='image/png')