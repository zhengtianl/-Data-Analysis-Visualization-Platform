import couchdb
import json 

file_path="./twitter-data-small.json"

masternode="172.26.133.182"
user='admin'
password='admin'
url = 'http://'+user+':'+password+'@'+masternode+':5984/'
couchclient = couchdb.Server(url)

name='twitter_full'
couchclient.create(name)
db = couchclient[name]
with open(file_path,'r', encoding='UTF-8') as f:
    data = json.load(f)
    print(f)
    for i in data:
        del i['_id']
        del i['_rev']
        db.save(i)
