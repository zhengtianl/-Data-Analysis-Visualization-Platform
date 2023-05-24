from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, requests, json,couchdb
couchdb_url = "http://172.26.133.182:5984"
username = "admin"
password = "admin"
database_name = "mas42_final"
batch = []
def savebatch(batch):
        url = f"{couchdb_url}/{database_name}/_bulk_docs"
        headers = {"Content-Type": "application/json"}
        data = {"docs": batch}
        response = requests.post(url, auth=(username, password), headers=headers, json=data)
        if response.status_code == 201:
            print("Batch documents stored successfully.")
        else:
            print(f"Failed to store batch documents. Error: {response.text}")


m = Mastodon(
        api_base_url=f'https://aus.social',
        access_token=os.environ['MASTODON_ACCESS_TOKEN']
    )
# Connect to the CouchDB server
couchclient = couchdb.Server('http://admin:admin@172.26.133.182:5984')
# Create or open the database
name='mas42_final'
try:
    couchclient.create(name)
    db = couchclient[name]
except: db = couchclient[name]

class Listener(StreamListener):
    def on_update(self, status):
        global batch
        obj = json.loads(json.dumps(status, indent=2, sort_keys=True, default=str))
        batch.append(obj)
        if len(batch) >= 50:
            savebatch(batch)
            batch = []

        
m.stream_public(Listener())


# item = {
#             'author_id': obj['account']['acct'],
#             'text': obj['content'],
#             'time':obj['created_at']
#             }
