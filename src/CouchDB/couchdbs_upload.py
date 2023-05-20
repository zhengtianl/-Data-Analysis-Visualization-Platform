import couchdb
import json
import requests
import os
import re
couchdb_url = "http://172.26.133.182:5984"
username = "admin"
password = "admin"
database_name = "tttt42"


def portion_load(chunk_size, rank):
    # Connect to the CouchDB server
    couchclient = couchdb.Server('http://admin:admin@172.26.133.182:5984')
    # Create or open the database
    name='tttt42'
    try:
        couchclient.create(name)
        db = couchclient[name]
    except: db = couchclient[name]
    

    # Calculate the start and end positions for each processor
    start_position = chunk_size*rank
    #确定结束为止 等同于下一个开始位置
    end_position = chunk_size*(rank+1)
    f.seek(start_position)
    batch = []
    if rank == 0:
        f.readline()
    while True:
            new_line = f.readline()
            # if f.tell()>=end_position:
            #     break
            if not new_line:
                savebatch(batch)
                break
            if new_line.endswith('}'):
                 kk = new_line
            else:
                 kk = new_line[:-2]
            tweet_json = json.loads(kk)
            batch.append(tweet_json)
            #把batch先录入
            if len(batch) >= 200:
                savebatch(batch)
                batch = []
                continue
    return None

def savebatch(batch):
    url = f"{couchdb_url}/tttt42/_bulk_docs"
    headers = {"Content-Type": "application/json"}
    data = {"docs": batch}
    response = requests.post(url, auth=(username, password), headers=headers, json=data)
    if response.status_code == 201:
        print("Batch documents stored successfully.")
    else:
        print(f"Failed to store batch documents. Error: {response.text}")




# Set the number of processors to use
# Open the JSON file
#with open('/data/mnt/ext100/twitter-huge.json', 'r') as f:
with open('/data/mnt/ext100/twitter-huge.json', 'r') as f:

    # Get the total size of the file
    file_size = f.seek(0,2)
    size = 3
    # Calculate the size to read for each processor
    chunk_size = file_size // size
    print(chunk_size)
    portion_load(chunk_size,0)
  
