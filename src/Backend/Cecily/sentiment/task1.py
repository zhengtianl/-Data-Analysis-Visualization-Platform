
import json
import pandas as pd
import re
from mpi4py import MPI
import os
import sys

with open('./twitter-data-small.json', 'r', encoding='utf-8') as data_file:
    data = json.load(data_file)

def Dotask1(iddata):
    iddic = {}
    for i in iddata:
        if i['data']['author_id'] in iddic.keys():
            iddic[i['data']['author_id']]+=1
        else:
            iddic[i['data']['author_id']] = 1
    return iddic






def outputTask1(processed1):
    big_dic = processed1[0]
    df = pd.DataFrame(columns=['ID', 'Number of Tweets Made'])
    for i in range(1, len(processed1)):
        for key, value in processed1[i].items():
            if key in big_dic:
                big_dic[key] += value
            else:
                big_dic[key] = value
    for i in big_dic.keys():
        new_row = {'ID':i,'Number of Tweets Made': big_dic[i]}
        new_row_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_row_df], ignore_index=True)
    final_df = df.sort_values(by=['Number of Tweets Made','ID'], ascending=False).head(10)
    final_df['rank'] = final_df['Number of Tweets Made'].rank(method='min',ascending=False).astype(int)
    final_df['rank'] = final_df['rank'].apply(lambda x: f'#{x}')
    final_df = final_df[['rank','ID','Number of Tweets Made']]
    print(final_df.to_string(index=False))
    return None

Dotask1(data)