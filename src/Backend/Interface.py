from flask import Flask, jsonify, send_file
import json
import pandas as pd
from flask_cors import CORS
import couchdb
import requests
import csv

from region_count import region_tweet_count
from sentiment_count import model
from alcohol import detect_alcohol,region
# from Server import city_count
# from word_cloud import word_cloud
from unemployment import get_rate


server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')
db_twitter= server['tttt42']
db_mastodon = server['mas42_final']

app = Flask(__name__)
CORS(app)


with open('citycountkey.json', 'r') as json_file:
    # Read the contents of the file
    json_data_1 = json_file.read()
    # Parse the JSON data
    data_key = json.loads(json_data_1)

with open('view_results.json', 'r') as json_file:
    # Read the contents of the file
    json_data = json_file.read()
    # Parse the JSON data
    data_all = json.loads(json_data)

with open('sentiment.json', 'r') as json_file:
    # Read the contents of the file
    json_data = json_file.read()
    # Parse the JSON data
    data_senti = json.loads(json_data)

with open('mastodon.json', 'r') as json_file:
    # Read the contents of the file
    json_data = json_file.read()
    # Parse the JSON data
    data_mas = json.loads(json_data)

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
    doc_list_tweet = []
    for row in data_all['rows']:
        doc_list_tweet.append(row)
    region_list_tweet = region(doc_list_tweet) 
    rank_tweet= region_tweet_count(doc_list_tweet, region_list_tweet)
    # region_list_mas = region(doc_list_mas) 
    # rank_mas= region_tweet_count(doc_list_mas, region_list_mas)
    return jsonify({'rank_tweet': rank_tweet,'region_list': region_list_tweet})


@app.route("/alcohol_detect", methods=["GET"])
def get_data_alcohol():
    doc_list_tweet = []
    for row in data_key['rows']:
        doc_list_tweet.append(row)
    region_list_tweet = region(doc_list_tweet)
    alcohol_count_tweet = detect_alcohol(doc_list_tweet, region_list_tweet)
    
    return jsonify({'alcohol_count_lga': alcohol_count_tweet,'lga_list': region_list_tweet})

#model is too big to run 1
# @app.route("/sentiment", methods=["GET"])
# def sentiment():
   
#     doc_list = []
#     for row in data_senti['rows']:
#         doc_list.append(row)
#     doc_list_mas = []
#     for row in data_mas['rows']:
#         doc_list_mas.append(row)
#     sentiment_detect = model(train_data, doc_list)
#     totol_amount = len(doc_list)
#     sentiment_detect_mas = model(train_data, doc_list_mas)
#     totol_amount_mas = len(doc_list_mas)
#     return jsonify({'sentiment_detect_tweet': sentiment_detect, 'total_amount_tweet':totol_amount,
#                     'sentiment_detect_mas': sentiment_detect_mas, 'total_amount_mas':totol_amount_mas})


@app.route("/unemployment", methods=["GET"])
def unemployment():
    doc_list_tweet = []
    for row in data_key['rows']:
        doc_list_tweet.append(row)
    region_list_tweet = region(doc_list_tweet)
    unemployment_rate_tweet = get_rate(doc_list_tweet, region_list_tweet)
    return jsonify({'unemploy_rate': unemployment_rate_tweet})

#test


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