import json
import pandas as pd
import re
import couchdb
import csv
import requests

server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')
db = server['test500']


view_url = 'http://admin:admin@172.26.133.182:5984/test500/_design/try/_view/countkey2?reduce=false'
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
                true_count = i['value']['count']
                return true_count



def get_rate(doc_list, region):
    rates = []  # 存储城市和rate的列表
    for i in region:
        one_suburb = i.lower()
        for item in unemploy_list:
            if item['lga_name16'].lower() == one_suburb:
                total_unemployment = item['p_unemp_tot']
                num_alcohol = detect_alcohol(doc_list, one_suburb)
                if num_alcohol is None:
                    rate = 0
                else:
                    rate = num_alcohol / total_unemployment

                # 将城市和rate添加到字典中
                result = {
                    'city': i,
                    'rate': rate
                }
                rates.append(result)  # 将字典添加到列表中

    return rates 
            

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

# def answer():
#     region_list = region(doc_list)
#     answer = get_total_unemployment(doc_list, region_list)
#     return print(answer)

# answer()
