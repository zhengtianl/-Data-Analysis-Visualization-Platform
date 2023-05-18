import json
import pandas as pd
import re
# from mpi4py import MPI
import os
import sys

import couchdb

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
    
def region_tweet_count(iddata, region):
    iddic = {}
    for i in iddata:
        for j in region:
            full_name = i['place']
            exact_name = full_name.lower().split(',')[0]
            if exact_name == j:
                if i['_id'] in iddic.keys():
                    iddic[i['_id']]+=1
                else:
                    iddic[i['_id']] = 1
    sorted_dict = dict(sorted(iddic.items(), key=lambda x: x[1], reverse=True))
    rank_items = list(sorted_dict.items())[:10]
        
    
    return rank_items


def region(id_data):
    region_list = []
    for i in id_data:
        full_name = i['place']
        exact_name = full_name.lower().split(',')[0]
        if exact_name not in region_list:
            region_list.append(exact_name)
        else:
            continue
    return region_list





