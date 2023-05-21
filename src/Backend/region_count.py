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
db = server['twitter_huge_loc_f']


view_url = 'http://172.26.133.182:5984/twitter_huge_loc_f/_design/new/_view/keywords?group=true'
response = requests.get(view_url, auth=('admin', 'admin'))
data = response.json()


doc_list = []
for row in data['rows']:
    doc_list.append(row)

print(doc_list[1])
# def region_tweet_count(iddata, region):
#     iddic = {}
#     for i in iddata:
#         for j in region:
#             if 'place' in i:
#                 full_name = i['place']
#                 exact_name = full_name.lower().split(',')[0]
#                 if exact_name == j:
#                     if i['_id'] in iddic.keys():
#                         iddic[i['_id']]+=1
#                     else:
#                         iddic[i['_id']] = 1
#     sorted_dict = dict(sorted(iddic.items(), key=lambda x: x[1], reverse=True))
#     rank_items = list(sorted_dict.items())[:10]
        
    
#     return rank_items


def region(id_data):
    region_list = []
    for i in id_data:
        if 'place' in i:
            full_name = i['place']
            exact_name = full_name.lower().split(',')[0]
            if exact_name not in region_list:
                region_list.append(exact_name)
            else:
                continue
    return region_list


# region_list = region(doc_list)
# print(region_tweet_count(doc_list, region_list))



