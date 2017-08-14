# consumer_key, consumer_secret, access_token and access_token_secret are stored here
from keys import *

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
