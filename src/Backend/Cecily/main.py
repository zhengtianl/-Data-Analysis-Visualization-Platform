import json
import pandas as pd
import re
from mpi4py import MPI
import os
import sys

with open('./twitter-data-small.json', 'r', encoding='utf-8') as data_file:
    id_data = json.load(data_file)
    
def region_tweet_count(iddata, region):
    iddic = {}
    for i in iddata:
        for j in region:
            if i['includes']['places'][0]['full_name'] == j:
                if i['data']['author_id'] in iddic.keys():
                    iddic[i['data']['author_id']]+=1
                else:
                    iddic[i['data']['author_id']] = 1
    sorted_dict = dict(sorted(iddic.items(), key=lambda x: x[1], reverse=True))
    rank_items = list(sorted_dict.items())[:10]
        
    
    return rank_items


def region(id_data):
    region_list = []
    for i in id_data:
        if i['includes']['places'][0]['full_name'] not in region_list:
            region_list.append(i['includes']['places'][0]['full_name'])
        else:
            continue
    return region_list
    


output = region_tweet_count(id_data,['New South Wales, Australia'])
region_list = region(id_data)

print(output)

