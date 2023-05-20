from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json,couchdb
seconds = 60
start_time = time.time()
end_time = start_time + seconds
m = Mastodon(
        api_base_url=f'https://aus.social',
        access_token=os.environ['MASTODON_ACCESS_TOKEN']
    )
# Connect to the CouchDB server
couchclient = couchdb.Server('http://admin:admin@172.26.133.182:5984')
    # Create or open the database
name='mastodon_large'
try:
    couchclient.create(name)
    db = couchclient[name]
except: db = couchclient[name]
class Listener(StreamListener):
    def on_update(self, status):
        obj = json.loads(json.dumps(status, indent=2, sort_keys=True, default=str))
        item = {
            'author_id': obj['account']['acct'],
            'text': obj['content'],
            'time':obj['created_at']
            }
        db.save(item)
m.stream_public(Listener())
