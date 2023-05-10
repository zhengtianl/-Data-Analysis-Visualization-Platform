"""test Flask with this"""
from flask import Flask, request
from flask_restful import Resource, Api
from flask import jsonify
import json
from flask_cors import CORS
# import sys
# sys.path.append('/path/to/main.py/directory') # 将main.py的目录添加到Python模块搜索路径中
from main import region_tweet_count, region # 导入main.py中的某个函数

app = Flask(__name__)
CORS(app)
api = Api(app)

# connect to the local CouchDB instance
#couch = couchdb.Server()

# get a reference to an existing database
#db = couch['mydatabase']

with open('./twitter-data-small.json', 'r', encoding='utf-8') as data_file:
    id_data = json.load(data_file)

@app.route("/api/data", methods=["GET"])
def get_data():
    region_area = region(id_data)
    tweet_count = region_tweet_count(id_data,region_area)
    return jsonify({'region':region_area, 'count':tweet_count})




if __name__ == '__main__':
     app.run(host='0.0.0.0',port='3000',debug=True)
