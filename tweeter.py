import tweepy
#instalar el paquete de la siguiente forma:  pip install tweepi
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # estos valores se dan al habilitar el servicio de tweeter de la cuenta.
  cfg = { 
    "consumer_key"        : "VALUE",
    "consumer_secret"     : "VALUE",
    "access_token"        : "VALUE",
    "access_token_secret" : "VALUE" 
    }

  api = get_api(cfg)
  tweet = "Hello, world! msg from an py app"
  status = api.update_status(status=tweet) 
 

if __name__ == "__main__":
  main()
