# consumer_key, consumer_secret, access_token and access_token_secret are stored here
from keys import *
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search, q='#sohrab').items(10):
    try:
        # Print out usernames of the last 10 people to use #ocean
        print('Tweet by: @' + tweet.user.screen_name)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
