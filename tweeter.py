import tweepy,psycopg2,os,json,datetime

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
#connstr para bd
conn_string = "host='localhost' dbname='sosagua' user='postgres' password='Guatemala1'"


# estos valores se dan al habilitar el servicio de tweeter de la cuenta.
cfg = { 
  "consumer_key"        : "bCgXMvHfVr1f86jrcwJSIbfyU",
  "consumer_secret"     : "UUYjGwM63n6UvZMPTmfZG0yUq5eDm2PE5747F0xht71pgr2g8v",
  "access_token"        : "1432847989-W3qw9szAWWP0VxsPpEsvVZX6igJjrVJzUZrrgYY",
  "access_token_secret" : "332CPmsifvklzEK33F99flSAde5zz71fCiaz4V1P6qYIs" 
  }


def insertaTwitt(tjson,tstr):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
#    cursor.execute(""" delete from test where campo1 = 'David'  """)
    cursor.execute(" insert into fase1 (twitt,twittstr) values (" + str(tjson) + ",'" + tstr + "')")
    #conn.commit()
    conn.close()



#instalar el paquete de la siguiente forma:  pip install tweepi
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def sendTwitt():
  api = get_api(cfg)
  tweet = "Hello, world! msg from an py app"
  status = api.update_status(status=tweet) 

class msg:
  def __init__(self, created_at, id, id_str, text, entities, metadata, source, user):
    self.created_at = created_at
    self.id = id
    self.id_str = id_str
    self.text = text
    self.entities = entities
    self.metadata = metadata
    self.source = source
    self.user = user
  

def getTweets(sw,date,number):
  api = get_api(cfg)
  search_words = sw#"#COVID2019"
  date_since = date
  tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(number)
  # Iterate and print tweets

  
  
  for item in tweets:
    s = item#este es el string
    #print(s)
      #print(tweet.text)
    #print(tweet.created_at)
    #print(tweet.id)
    #print(tweet.id_str)
    #print(tweet.text)
    #print(tweet.entities)
    #print(tweet.metadata)
    #print(tweet.source)
    #print(tweet.user)
    #m = msg(tweet.created_at,tweet.id,tweet.id_str,tweet.text,tweet.entities,tweet.metadata,tweet.source,tweet.user)#este sera el json
    #json.dumps(m)
    #print(m)
    mined = {
                    'id':        item.id,
                    'name':            item.user.name,
                    'screen_name':     item.user.screen_name,
                    'retweet_count':   item.retweet_count,
                    'text':            item.text,
                    'mined_at':        datetime.datetime.now(),
                    'created_at':      item.created_at,
                    'favourite_count': item.favorite_count,
                    'hashtags':        item.entities['hashtags'],
                    'status_count':    item.user.statuses_count,
                    'location':        item.place,
                    'source':   item.source
                }
    print(mined)
    #insertaTwitt(mined,s)

if __name__ == "__main__":
  #sendTwitt()
  getTweets("#COVID2019","2020-02-16",1)
