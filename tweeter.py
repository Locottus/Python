import tweepy,psycopg2,os,json,datetime

'''
HERLICH STEVEN GONZALEZ ZAMBRANO 2020 --> EN CUARENTENA MUNDIAL
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

#****************************************FASE 1 *******************************************

'''

update pg_database set encoding=8 where datname='sosagua';
update pg_database set encoding = pg_char_to_encoding('UTF8') where datname = 'sosagua'
	
create table public.fase1(
	id SERIAL PRIMARY KEY,
	fecha timestamp without time zone DEFAULT now(),
	twitjson json not null ,
	twitstring text not null ,
	origen text null
)

'''

def insertaTwitt(tjson,tstr):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print(tjson)
#    cursor.execute(""" delete from test where campo1 = 'David'  """)
    cursor.execute(" insert into fase1 (twitjson,twitstring,origen) values ('" + json.dumps(tjson) + "','" + str(tstr).replace("'",'"') + "','Twitter')")
    conn.commit()
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
  

def getTweets(search_words,date_since,number):
  api = get_api(cfg)
  #"#COVID2019"
  tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="es",
              since=date_since).items(number)
  # Iterate and print tweets
  
  for item in tweets:
    s = item#este es el string
    #m = msg(tweet.created_at,tweet.id,tweet.id_str,tweet.text,tweet.entities,tweet.metadata,tweet.source,tweet.user)#este sera el json
    #json.dumps(m)
    mined = {
                    "id":              item.id,
                    "name":            item.user.name,
                    "screen_name":     item.user.screen_name,
                    "retweet_count":   item.retweet_count,
                    "text":            convUTF8(item.text),
                    "location":        convUTF8(item.user.location),
                    "coordinates":     str(item.coordinates),
                    "geo_enabled":     str(item.user.geo_enabled),
                    "geo":             str(item.geo),
                    "created_at":      str(item.created_at),
                    "favorite_count": item.favorite_count,
                    "hashtags":        item.entities['hashtags'],
                    "status_count":    item.user.statuses_count,
                    "place":           convUTF8(item.place),
                    "source":          item.source
                }
    #print(mined)
    #minedS = minedS.replace("'",'"')
    insertaTwitt(str(mined).replace("'",'"'),s)

def getToday():
    from datetime import date
    return date.today()

def convUTF8(cadena):
    return str(cadena).replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","Ñ")



#****************************FASE 2******************************************

'''
create table public.fase2(
	id SERIAL PRIMARY KEY,
	fecha timestamp without time zone DEFAULT now(),
	fase1 numeric not null ,
	municipios numeric null
);

create table public.categorias(
        id SERIAL PRIMARY KEY,
	fecha timestamp without time zone DEFAULT now(),
	twitstring text not null ,
);

'''


def getLocation():
    from psycopg2.extras import RealDictCursor
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("select cast(id as text), pais,departamen_1,municipi_1,cast(point_x as text),cast(point_y as text) from public.municipios")
    l = json.dumps(cursor.fetchall(),indent = 2)
    conn.close()
    #print(l)  
    return l

def fase2(fecha):
    query = "insert into public.fase2 ( municipios , fase1 )  select m1.id,fase1.id   from municipios m1, municipios m2, fase1 where m1.id = m2.id  and fase1.twitstring like '%' || m1.departamen_1 || '%' and fase1.twitstring like '%' || m2.municipi_1 || '%' and fase1.fecha > '" + fecha + " 00:00:00' "
    print(query)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("terminada fase 2")
    

if __name__ == "__main__":
  print("FASE 1 --> CONECTANDO A TWITTER PARA EXTRAER TWITS DEL DIA")
  #getTweets("#traficogt","2020-04-06",50)
  print('FASE 2 --> AGREGANDO COORDENADAS AL QUERY')
  #fase2("2020-04-06")  
  print('FASE 3 --> BUSCANDO PALABRAS CLAVE PARA CLASIFICACION')
#select fase2.id, municipios.point_x, municipios.point_y from fase2, municipios where municipios.id = fase2.municipios

