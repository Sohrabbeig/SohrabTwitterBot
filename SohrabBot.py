# consumer_key, consumer_secret, access_token and access_token_secret are stored here
from keys import *
import tweepy
from pymongo import MongoClient
from time import sleep


class SohrabBot(object):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    WELCOME_TEXT = "سلام دوست عزیز، خیلی خوش حالم از آشناییت!"

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.SohrabBot
        self.followers = self.db.followers

    def follow_back(self):
        while True:
            follower_ids = self.api.followers_ids()
            for f_id in follower_ids:
                if self.followers.find_one({"id_str": str(f_id)}) is None:
                    user = self.api.get_user(f_id)
                    self.followers.insert_one(user._json)
                    self.api.create_friendship(f_id)
                    user.status.retweet()
                    user.status.favorite()
                    self.api.send_direct_message(f_id, text=self.WELCOME_TEXT)
            sleep(300)
