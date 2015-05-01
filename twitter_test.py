from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json

#consumer key, consumer secret, access token, access secret
ckey="7sKBF7yJp9zRoyp42fw7DabOi"
csecret="ITMjCwMq9QQhGG3lMsMGh4I6Fgkfuj4LuDkc161G4Q268h0u8G"
atoken="16914991-sz5ocOxjDmHgzCSx81AgH7Fi7Pp5ekrp7wLNZJt7S"
asecret="220w8mGcwBaqAUB3rGP8U8vyYBZ4u4R0Bj4mzer6JGepW"

# replace mysql.server with "localhost" if you are running via your own server!
# server MySQL username MySQL pass Database name.
conn = MySQLdb.connect("mysql.server","beginneraccount","cookies","beginneraccount$tutorial")
c = conn.cursor()

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        
        username = all_data["user"]["screen_name"]
        
        c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))
        
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])