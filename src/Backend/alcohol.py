# only use twitter-data
import re
import json
import couchdb
import requests

server = couchdb.Server('http://172.26.133.182:5984/')
server.resource.credentials = ('admin', 'admin')
db = server['mas42_final']


view_url = 'http://admin:admin@172.26.133.182:5984/mas42_final/_design/new/_view/sentiment?reduce=false'
response = requests.get(view_url, auth=('admin', 'admin'))
data = response.json()
# 将文档转换为字典列表

doc_list = []
for row in data['rows']:
    doc_list.append(row)

print(doc_list[1])
def detect_alcohol(doc_list, region):
    lst = []
    for i in doc_list:
        for j in region:
            if i['key'] is not None:
                full_name = i['key']
                if full_name is not None:
                    exact_name = full_name.lower().split(',')[0]
                if exact_name == j.lower():
                    true_count = i['value']
                    lst.append({'city': exact_name, 'count': true_count})
            
    return lst



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


region_list = region(doc_list)
print(detect_alcohol(doc_list, region_list))