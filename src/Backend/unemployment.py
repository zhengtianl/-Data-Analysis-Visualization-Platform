import json
import pandas as pd
import re
import couchdb
import csv
import requests
import itertools

with open('citycountkey.json', 'r') as json_file:
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




def detect_alcohol(doc_list, region):
    lst = []
    for i in doc_list:
        for j in region:
                full_name = i['key']
                if full_name is not None:
                    exact_name = full_name.lower().split(',')[0]
                if exact_name == j.lower():
                    true_count = i['value']['count']
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


def get_rate(doc_list, region):
    rates = []
    for suburb in region:
        one_suburb = suburb.lower()
        for item in unemploy_list:
            if item['lga_name16'].lower() == one_suburb:
                total_unemployment = item['p_unemp_tot']
                alcohol_detect = detect_alcohol(doc_list, region)
                for i in alcohol_detect:
                    if i['city'] == one_suburb:
                        num_alcohol = i['count']

                        result = {
                            'city': suburb,
                            'total_unemployment': total_unemployment,
                            'num_alcohol': num_alcohol
                        }
                        rates.append(result)
    return rates


            




# region_list = region(doc_list)
# print(get_rate(doc_list, region_list))
# num_alcohol = detect_alcohol(doc_list, region_list)
# print(type(num_alcohol[1]['count']))