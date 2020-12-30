from credentials import *    # This will allow us to use the keys as variables

#from pandas.io.json import json_normalize
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

# We create a tweet list as follows:
tweets = extractor.user_timeline(screen_name=user, count=200,include_rts=False)
print("Number of tweets extracted: {}.\n".format(len(tweets)))

data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
#data['USER']   = np.array([tweet.user for tweet in tweets])
data['CONTRIB']   = np.array([tweet.contributors for tweet in tweets])
data['COORD']   = np.array([tweet.coordinates for tweet in tweets])
data['GEO']   = np.array([tweet.geo for tweet in tweets])
data['PLACE']   = np.array([tweet.place for tweet in tweets])
data['ENTITIES']   = np.array([tweet.entities for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])


#display(data.head(10))

if not os.path.exists('./output/'):
    os.makedirs('./output/')

data.to_csv('./output/' + user + '_tweets.csv')
