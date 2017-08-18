# consumer_key, consumer_secret, access_token and access_token_secret are stored here
from keys import *
import tweepy
from time import sleep


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='#underscore62').items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        if not tweet.user.following:
            # Follow the user who tweeted
            tweet.user.follow()
            print('Followed the user')

        sleep(5)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break