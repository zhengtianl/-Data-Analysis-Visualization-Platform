import json
import pandas as pd
import re
import couchdb
import csv
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



def detect_alcohol(doc_list, region):
    for i in doc_list:
        for j in region:
            full_name = i['key']
            exact_name = full_name.lower().split(',')[0]
            if exact_name == j.lower():
                true_count = i['value']
    return true_count



def get_total_offences(region):
    for i in region:
        one_suburb = i.lower()
        for item in unemploy_list:
            if item['lga_name16'].lower() in region:
                total_umemployment = item['p_unemp_tot']
                num_alcohol = detect_alcohol(doc_list, region)
                rate = num_alcohol/total_umemployment
                return rate

print(get_total_offences(['cairns']))


