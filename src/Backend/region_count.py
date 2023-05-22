import json
import pandas as pd
import re
# from mpi4py import MPI
import os
import sys
import csv
import couchdb
import requests
import itertools

with open('view_results.json', 'r') as json_file:
    # Read the contents of the file
    json_data = json_file.read()
    # Parse the JSON data
    data = json.loads(json_data)


doc_list = []
for row in data['rows']:
     doc_list.append(row)


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


def region_tweet_count(doc_list, region):       
    lst = []
    for i in doc_list:
        for j in region:
                full_name = i['key']
                if full_name is not None:
                    exact_name = full_name.lower().split(',')[0]
                    if exact_name == j.lower():
                        true_count = i['value']
                        lst.append({'city': exact_name, 'count': true_count})
    lst.sort(key=lambda x: x['city'])  # Sort by 'city' for grouping
    grouped_lst = []
    for city, group in itertools.groupby(lst, key=lambda x: x['city']):
        count_list = [item['count'] for item in group]
        total_count = sum(count_list)
        grouped_lst.append({'city': city, 'count': total_count})
    grouped_lst_sorted = sorted(grouped_lst, key=lambda x: x['count'], reverse=True)
    return grouped_lst_sorted


def region(id_data):
    region_list = []
    for i in id_data:
        full_name = i['key']
        exact_name = full_name.lower().split(',')[0]
        for row in unemploy_list:
            if exact_name == row['lga_name16'].lower().strip():
                if exact_name not in region_list:
                    region_list.append(exact_name)
                else:
                    continue
    return region_list



# region_list = region(doc_list)
# print(region_tweet_count(doc_list, region_list))



