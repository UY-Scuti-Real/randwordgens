import tweepy
import spaceshipnamegenerator as namegen
import time
from apikeys import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print("got auth stuff")
user = api.me()

test = False
wipe = False
print("starting...")
if __name__ == "__main__":
    while 1:
        if wipe:
            print("deleting tweets")
            tweets= api.user_timeline(id=user.id, include_rts=True)
            for tweet in tweets :
                 api.destroy_status(tweet.id)
            print("yeeted deleted tweets")
            time.sleep(60*5)
        if time.strftime("%H") == '09'  or time.strftime('%H') == '21' and not test:
            print("sending tweet")
            string = namegen.gen_num(5, 'HMS')
            api.update_status(string)
            time.sleep(60*60*1.5)
