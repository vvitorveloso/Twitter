from credentials import *    # This will allow us to use the keys as variables

import json
from pandas.io.json import json_normalize

import sys
import os

user=sys.argv[1]


def twitter_setup():
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Return API with authentication:
    api = tweepy.API(auth)
    return api


# We create an extractor object:
extractor = twitter_setup()

user_info = extractor.get_user(screen_name=user)
data = json_normalize(user_info._json)

if not os.path.exists('./output/'):
    os.makedirs('./output/')

data.to_csv('./output/' + user + '_info.csv')


