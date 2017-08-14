# consumer_key, consumer_secret, access_token and access_token_secret are stored here
from keys import *
from time import sleep
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file verne.txt (or your chosen file) for reading
my_file = open('verne.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
    try:
        print(line)

        # Add if statement to ensure that blank lines are skipped
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)

    # Add sleep method to space tweets by 5 seconds each
    sleep(5)
