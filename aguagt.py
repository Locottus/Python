import tweepy, psycopg2, os, json, datetime,sys

f = open("sosagua.txt", "a")
#connstr para bd
#dev str
conn_string = "host='localhost' dbname='sosagua' user='postgres' password='Guatemala1'"

#produccion str
#conn_string = "host='localhost' dbname='sosagua' user='postgres' password='postgres2020!Incyt'"

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
	origen text null,
	municipio numeric null default 0,
	necesidad numeric null default 1
)


create table cubo1(
	municipio numeric not null,
	necesidad numeric not null,
	mes	text	not null,
	ano text	not null,
	contador numeric not null
)

'''

def insertaTwitt(tjson,tstr):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print(tjson)
        cursor.execute(" insert into fase1 (fecha,twitjson,twitstring,origen) values (now() - INTERVAL '1 DAY','" + json.dumps(tjson) + "','" + str(tstr).replace("'",'"') + "','Twitter')")
        conn.commit()
        conn.close()
    except:
        print("error en insertaTwitt")


#instalar el paquete de la siguiente forma:  pip install tweepi
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def sendTwitt():
  try:
      api = get_api(cfg)
      tweet = "Hello, world! msg from an py app"
      status = api.update_status(status=tweet) 
  except:
      print("twitt not send")


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
  try:
      api = get_api(cfg)
      #"#COVID2019"
      tweets = tweepy.Cursor(api.search,
                  q=search_words,
                  lang="es",
                  since=date_since).items(number)
      # Iterate and print tweets
      
      for item in tweets:
        try:
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
        except:
            print("un json viene malformado")

  except:
      print("getTweets error")


def getProcessDate():
    try:

        from datetime import date
        today = date.today()
        yesterday = today - datetime.timedelta(days=1)
        return yesterday
    except:
        print("error en getProcessDate")
        
def convUTF8(cadena):
    try:
        return str(cadena).replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","Ñ")
    except:
        return cadena


#****************************FASE 2******************************************

'''

create table public.necesidad(
        id SERIAL PRIMARY KEY,
	descripcion text not null
	
);

create table public.sinonimos(
        necesidad numeric,
        sinonimo text not null unique
	
);



'''

def write(cadena):
    try:
        f.write(str(cadena) + '\n')
    except:
        print("could not write")

        
def getLocation():
    try:
        from psycopg2.extras import RealDictCursor
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("select cast(id as text), pais,departamen_1,municipi_1,cast(point_x as text),cast(point_y as text) from public.municipios")
        l = json.dumps(cursor.fetchall(),indent = 2)
        conn.close()
        return l
    except:
        print("error en getLocation")

def ejecutaComandoPsql(query):
    try:
        #query = "insert into public.fase2 ( municipios , fase1 )  select distinct m1.id,fase1.id   from municipios m1, municipios m2, fase1 where m1.id = m2.id  and fase1.twitstring like '%' || m1.departamen_1 || '%' and fase1.twitstring like '%' || m2.municipi_1 || '%' and fase1.fecha > '" + fecha + " 00:00:00' "
        #query = "update fase1  set municipio = m1.id   from municipios m1, municipios m2 where m1.id = m2.id  and fase1.twitstring like '%' || m1.departamen_1 || '%' and fase1.twitstring like '%' || m2.municipi_1 || '%' and fase1.fecha > '" + fecha + " 00:00:00' "
        print(query)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
    except:
        print("error en ejecutar comando psql")


#ADD HERE NEW HASHTAGS
hashtags = ["#AGUAGT", "#SOSAGUAGT", "#SINAGUA"]
#hashtags = ["#TRANSITOGT"]
nTwits = 50000

if __name__ == "__main__":
  write("*************************************************************")
  fecha = getProcessDate()
  print(fecha)
  write(fecha)
  print("FASE 1.0 --> CONECTANDO A TWITTER PARA EXTRAER TWITS DEL DIA")
  
  for x in hashtags:
      print(x)
      write(x)
      try:
          getTweets(x,str(fecha),nTwits)
      except:
          print("error en for de los hashtags, se procede a las fases")




  print('FASE 1.2 --> AGREGANDO COORDENADAS DE MUNICIPIOS AL QUERY')
  write('FASE 1.2 --> AGREGANDO COORDENADAS DE MUNICIPIOS AL QUERY')

  #query = "update fase1  set municipio = m1.id   from municipios m1, municipios m2 where m1.id = m2.id  and lower(fase1.twitstring) like '%' || lower(m1.departamen_1) || '%' and lower(fase1.twitstring) like '%' || lower(m2.municipi_1) || '%' and fase1.fecha > '" + str(fecha) + " 00:00:00' "
  query = "update fase1  set municipio = m1.id from  municipios m1 where lower(fase1.twitstring) like '%' || lower(m1.departamen_1) || '%' and fase1.municipio = 0  and fase1.fecha > '" + str(fecha) + " 00:00:00' "
  ejecutaComandoPsql(query)

  query = "update fase1  set municipio = m1.id from  municipios m1 where lower(fase1.twitstring) like '%' || lower(m1.municipi_1) || '%'  and fase1.municipio = 0  and fase1.fecha > '" + str(fecha) + " 00:00:00' "
  ejecutaComandoPsql(query)

  print('FASE 1.3 --> BUSCANDO PALABRAS CLAVE PARA CLASIFICACION --> CREANDO CUBO 1')
  write('FASE 1.3 --> BUSCANDO PALABRAS CLAVE PARA CLASIFICACION --> CREANDO CUBO 1')

  query = "update fase1 set municipio = 0 where municipio is null"
  ejecutaComandoPsql(query)

#TODO QUERY NECESIDAD
  query = "update fase1  set necesidad = s1.necesidad from  sinonimos s1 where lower(fase1.twitstring) like '%' || lower(s1.sinonimo) || '%'  "
  ejecutaComandoPsql(query)#TODO where current month and current year
  
  query = "update fase1 set necesidad = 0 where necesidad is null"
  ejecutaComandoPsql(query)
  query = "delete from cubo1"#TODO where current month and current year
  ejecutaComandoPsql(query)
  query = "insert into cubo1 (municipio,necesidad,mes,ano,contador) select municipio, necesidad, extract(MONTH from FECHA),extract (YEAR from FECHA), count(*) from fase1 group by municipio, necesidad,  extract(MONTH from FECHA), extract(YEAR from FECHA)"
  ejecutaComandoPsql(query)#TODO where current month and current year

  print("proceso terminado")
  write("proceso terminado")
  f.close()



