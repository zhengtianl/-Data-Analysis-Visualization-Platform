import json
import pandas as pd
from collections import Counter, defaultdict
from mpi4py import MPI

tweet_file = 'twitter-data-small.json'
sal_file = 'sal.json'
city_dict = {}
author_cnt_dict = Counter()
author_city_dict = {}
city_cnt_dict = {"1gsyd": 0, '2gmel': 0, '3gbri': 0, '4gade': 0, '5gper': 0, '6ghob': 0, '7gdar': 0, '8acte':0, '9oter':0}

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

with open('sal.json','r', encoding= 'utf-8') as sal_data:
    sal_data = json.load(sal_data)
    for location in sal_data.keys():
        if sal_data.get(location).get('gcc')[1] != 'r':
            city_dict[location] = sal_data.get(location).get('gcc')

def process(tweet):
    author_id = tweet.get('data').get('author_id')
    full_name = tweet.get('includes').get('places')[0].get('full_name')
    full_name = full_name.split(',')[0].lower()
    if full_name in city_dict.keys():
        city = city_dict[full_name]
        city_cnt_dict[city] += 1
        if author_id in author_cnt_dict.keys():
            author_cnt_dict[author_id] += 1
        else:
            author_cnt_dict[author_id] = 1
        if author_id not in author_city_dict.keys():
            author_city_dict[author_id] = {
                                        "1gsyd": 0,
                                        '2gmel': 0,
                                        '3gbri': 0,
                                        '4gade': 0,
                                        '5gper': 0,
                                        '6ghob': 0,
                                        '7gdar': 0,
                                        '8acte': 0,
                                        '9oter': 0
                                    }
        author_city_dict[author_id][city] += 1
        return author_cnt_dict, author_city_dict, city_cnt_dict

with open(tweet_file, 'r') as tweet_file:
    total_bytes = tweet_file.seek(0,2)
    each_bytes = total_bytes // size
    begin_position = rank * each_bytes
    end_position = (rank + 1) * each_bytes
    tweet_str = ''
    tweet_file.seek(begin_position)
    while True:
        new_line= tweet_file.readline()
        if new_line == '  },\n' or new_line == '  }\n':
            tweet_str += new_line.split(',')[0]
            try:
                tweet_json = json.loads(tweet_str)
                process(tweet_json)
            except:
                text_str = ""
            if tweet_file.tell() >= end_position:
                break
            tweet_str = ""
        elif not new_line:
            break
        else:
            tweet_str += new_line
    city_cnt_dict_list = comm.gather(city_cnt_dict, root=0)
    author_cnt_dict_list = comm.gather(author_cnt_dict, root = 0)
    author_city_dict_list = comm.gather(author_city_dict, root = 0)
if rank == 0:
    for key in city_cnt_dict.keys():
        for i in range(1,size):
            city_cnt_dict[key] += city_cnt_dict_list[i][key]
    # print(city_cnt_dict)
    for key in author_cnt_dict.keys():
        for i in range(1,size):
            author_cnt_dict[key] += author_cnt_dict_list[i][key]

    for i in range(1, size):
        for author_id in author_city_dict_list[i].keys():
            if author_id not in author_city_dict:
                author_city_dict[author_id] = {
                    "1gsyd": 0,
                    '2gmel': 0,
                    '3gbri': 0,
                    '4gade': 0,
                    '5gper': 0,
                    '6ghob': 0,
                    '7gdar': 0,
                    '8acte': 0,
                    '9oter': 0
                }
            for city in author_city_dict_list[i][author_id].keys():
                author_city_dict[author_id][city] += author_city_dict_list[i][author_id][city]

def formal_task1(city_cnt_dict):
    location_counts = city_cnt_dict
    location_counts_list = [(k, v) for k, v in location_counts.items()]
    sorted_location_counts_list = sorted(location_counts_list, key=lambda x: x[1], reverse=True)
    df = pd.DataFrame(sorted_location_counts_list, columns=['Greater Capital City', 'Number of Tweets Made'])
    return (df.to_string(index=False))
def formal_task2(author_cnt_dict, num_tweeters=10):
    top_tweeters = author_cnt_dict.most_common(num_tweeters)
    df = pd.DataFrame(top_tweeters, columns=['Author ID', 'Number of Tweets'])
    df.insert(0, 'Rank', ['#' + str(i + 1) for i in range(len(top_tweeters))])
    return (df.to_string(index=False))

def formal_task3(author_city_dict):
    author_city_counts = {
        author_id: sum(city_dict.values()) for author_id, city_dict in author_city_dict.items()
    }
    sorted_author_city_counts = sorted(author_city_counts.items(), key=lambda x: (sum(1 for count in author_city_dict[x[0]].values() if count > 0), x[1]), reverse=True)[:10]
    data = []
    for rank, (author_id, city_counts) in enumerate(sorted_author_city_counts, start=1):
        nonzero_count = sum(1 for count in author_city_dict[author_id].values() if count > 0)
        city_counts_str = ",".join(
            [f"{count} {loc[1:]}" for loc, count in author_city_dict[author_id].items() if count > 0])
        data.append({"Rank":f"#{rank}", "Author Id":author_id,
                     "Number of Unique City Locations and #Tweets": f"{nonzero_count}(#{city_counts}tweets-{city_counts_str})"})
    df = pd.DataFrame(data)
    return (df.to_string(index=False))

if rank == 0:
    print(formal_task1(city_cnt_dict))
    print()
    print(formal_task2(author_cnt_dict))
    print()
    print(formal_task3(author_city_dict))
    print()