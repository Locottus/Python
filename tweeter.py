'''
API key:
bCgXMvHfVr1f86jrcwJSIbfyU

API secret key:
UUYjGwM63n6UvZMPTmfZG0yUq5eDm2PE5747F0xht71pgr2g8v

access token
1432847989-W3qw9szAWWP0VxsPpEsvVZX6igJjrVJzUZrrgYY


access token secret
332CPmsifvklzEK33F99flSAde5zz71fCiaz4V1P6qYIs

'''
# estos valores se dan al habilitar el servicio de tweeter de la cuenta.
cfg = { 
  "consumer_key"        : "bCgXMvHfVr1f86jrcwJSIbfyU",
  "consumer_secret"     : "UUYjGwM63n6UvZMPTmfZG0yUq5eDm2PE5747F0xht71pgr2g8v",
  "access_token"        : "1432847989-W3qw9szAWWP0VxsPpEsvVZX6igJjrVJzUZrrgYY",
  "access_token_secret" : "332CPmsifvklzEK33F99flSAde5zz71fCiaz4V1P6qYIs" 
  }


import tweepy
#instalar el paquete de la siguiente forma:  pip install tweepi
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def sendTwitt():
  api = get_api(cfg)
  tweet = "Hello, world! msg from an py app"
  status = api.update_status(status=tweet) 


def getTweets(number):
  api = get_api(cfg)
  search_words = "#COVID2019"
  date_since = "2020-02-16"
  tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(number)
  # Iterate and print tweets
  for tweet in tweets:
      #print(tweet.text) 
    print(tweet)


if __name__ == "__main__":
  #sendTwitt()
  getTweets(10)
