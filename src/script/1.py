from mastodon import Mastodon, MastodonNotFoundError, MastodonRatelimitError, StreamListener
import csv, os, time, json

m = Mastodon(
        api_base_url=f'https://aus.social',
        access_token=os.environ['MASTODON_ACCESS_TOKEN']
    )

class Listener(StreamListener):
    def on_update(self, status):
        obj = json.loads(json.dumps(status, indent=2, sort_keys=True, default=str))
        print(obj["content"])

m.stream_public(Listener())
