from flask import Flask, jsonify
import json
import pandas as pd
from flask_cors import CORS
from region_count import region_tweet_count, region
from sentiment_count import model
from alcohol import detect_alcohol
from Server import city_count
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

@app.route("/count", methods=["GET"])
def count():
    region_area = region(id_data)
    tweet_count = region_tweet_count(id_data, region_area)
    return jsonify({'region': region_area, 'count': tweet_count})

@app.route("/city_count", methods=["GET"])
def city_count_amount():
    city_count_dict = city_count(sal_data)
    return city_count_dict


@app.route("/alcohol", methods=["GET"])
def alcohol():
    region_area = region(id_data)
    alcohol_count = detect_alcohol(id_data, region_area)
    return jsonify({'region': region_area, 'alcohol_count': alcohol_count})


@app.route("/sentiment", methods=["GET"])
def sentiment():
    sentiment_list = model(train_data, id_data)
    return jsonify({'sentiment_list': sentiment_list})

