from flask import Flask, jsonify, send_file
import json
import pandas as pd
from flask_cors import CORS
import couchdb
import requests
import csv

from region_count import region_tweet_count, region
from sentiment_count import model
from alcohol import detect_alcohol,region
# from Server import city_count
# from word_cloud import word_cloud
from unemployment import get_total_unemployment,unemploy_list,detect_alcohol


server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')
db_twitter= server['test500']
db_mastodon = server['mas42_final']

app = Flask(__name__)
CORS(app)


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


with open('Train.csv', 'r') as file:
    train_data = pd.read_csv(file, sep=',')

with open('Test.csv', 'r') as file:
    test_data = pd.read_csv(file, sep=',')




@app.route("/rank", methods=["GET"])
def get_total_unemployment():
    view_url_tweet = 'http://admin:admin@172.26.133.182:5984/test500/_design/try/_view/countkey2?reduce=false'
    response_tweet = requests.get(view_url_tweet, auth=('admin', 'admin'))
    data_tweet = response_tweet.json()
    doc_list_tweet = []
    for row in data_tweet['rows']:
        doc_list_tweet.append(row)
    #data for mastodon#
    # view_url_mastodon = 'http://admin:admin@172.26.133.182:5984/mas42_final/_design/new/_view/sentiment?reduce=false'
    # response_mas = requests.get(view_url_mastodon, auth=('admin', 'admin'))
    # data_mas = response_mas.json()
    # doc_list_mas = []
    # for row in data_mas['rows']:
    #     doc_list_mas.append(row)
    region_list_tweet = region(doc_list_tweet) 
    rank_tweet= region_tweet_count(doc_list_tweet, region_list_tweet)
    # region_list_mas = region(doc_list_mas) 
    # rank_mas= region_tweet_count(doc_list_mas, region_list_mas)
    return jsonify({'rank_tweet': rank_tweet})


@app.route("/alcohol_detect", methods=["GET"])
def get_data_alcohol():
    view_url_tweet = 'http://admin:admin@172.26.133.182:5984/test500/_design/try/_view/countkey2?reduce=false'
    response_tweet = requests.get(view_url_tweet, auth=('admin', 'admin'))
    data_tweet = response_tweet.json()
    doc_list_tweet = []
    for row in data_tweet['rows']:
        doc_list_tweet.append(row)
    region_list_tweet = region(doc_list_tweet)
    alcohol_count_tweet = detect_alcohol(doc_list_tweet, region_list_tweet)

    #data for mastodon
    # view_url_mastodon = 'http://admin:admin@172.26.133.182:5984/mas42_final/_design/new/_view/sentiment?reduce=false'
    # response_mas = requests.get(view_url_mastodon, auth=('admin', 'admin'))
    # data_mas = response_mas.json()
    # doc_list_mas = []
    # for row in data_mas['rows']:
    #     doc_list_mas.append(row)

    # region_list_tweet = region(doc_list_tweet)
    # alcohol_count_tweet = detect_alcohol(doc_list_tweet, region_list_tweet)

    # region_list_mas = region(doc_list_mas)
    # alcohol_count_mas = detect_alcohol(doc_list_mas, region_list_mas)
    return jsonify({'alcohol_count_twitter': alcohol_count_tweet})


@app.route("/sentiment", methods=["GET"])
def sentiment():
    view_url_mastodon = 'http://admin:admin@172.26.133.182:5984/mas42_final/_design/new/_view/sentiment?reduce=false'
    response_mas = requests.get(view_url_mastodon, auth=('admin', 'admin'))
    data_mas = response_mas.json()
    doc_list_mas = []
    for row in data_mas['rows']:
        doc_list_mas.append(row)
    sentiment_detect_mas = model(train_data, doc_list_mas)
    totol_amount_mas = len(doc_list_mas)
    return jsonify({'sentiment_detect_mas': sentiment_detect_mas, 'total_amount_mas':totol_amount_mas})


@app.route("/unemployment", methods=["GET"])
def unemployment():
    view_url_tweet= 'http://admin:admin@172.26.133.182:5984/test500/_design/try/_view/countkey2?reduce=false'
    response_tweet = requests.get(view_url_tweet, auth=('admin', 'admin'))
    data_tweet = response_tweet.json()
    doc_list_tweet = []
    for row in data_tweet['rows']:
        doc_list_tweet.append(row)
    region_list_tweet = region(doc_list_tweet)
    unemployment_rate_tweet = get_total_unemployment(doc_list_tweet, region_list_tweet)
    return jsonify({'unemploy_rate': unemployment_rate_tweet})




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