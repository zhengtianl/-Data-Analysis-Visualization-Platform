import json
import pandas as pd
import re
# from mpi4py import MPI
import os
import sys

import couchdb
import requests

server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')
db = server['test500']


view_url = 'http://admin:admin@172.26.133.182:5984/test500/_design/try/_view/countkey2?reduce=false'
response = requests.get(view_url, auth=('admin', 'admin'))
data = response.json()

# view_url_mastodon = 'http://admin:admin@172.26.133.182:5984/mas42_final/_design/new/_view/sentiment?reduce=false'
# response_mas = requests.get(view_url_mastodon, auth=('admin', 'admin'))
# data_mas = response_mas.json()
# doc_list_mas = []
# for row in data_mas['rows']:
#     doc_list_mas.append(row)

doc_list = []
for row in data['rows']:
    doc_list.append(row)


def region_tweet_count(doc_list, region):
    iddic = {}
    for i in doc_list:
        for j in region:
            if 'key' in i:
                full_name = i['key']
                exact_name = full_name.lower().split(',')[0]
                if exact_name == j:
                    if i['id'] in iddic.keys():
                        iddic[i['id']]['count'] += 1
                    else:
                        iddic[i['id']] = {'count': 1, 'region': exact_name}
    sorted_dict = dict(sorted(iddic.items(), key=lambda x: x[1]['count'], reverse=True))
    rank_items = list(sorted_dict.items())[:10]
    return rank_items
        
    



def region(id_data):
    region_list = []
    for i in id_data:
        if i['key'] is not None:
            full_name = i['key']
            exact_name = full_name.lower().split(',')[0]
            if exact_name not in region_list:
                region_list.append(exact_name)
            else:
                continue
    return region_list


# region_list = region(doc_list)
# print(region_tweet_count(doc_list, region_list))



