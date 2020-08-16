import os,sys, psycopg2, datetime

conn_string = "host='localhost' dbname='sosguate' user='postgres' password='Guatemala1'"


def hacequery():
    #print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)
    #get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("""select * from test""")
    rows = cursor.fetchall()
 
    for row in rows:
        rString = "{'name':" + row[0] +",'lastname':" + row[1] +",'status':" + str(row[2]) + "}"
        
        #print "   ", row[0],row[1],row[2]
    conn.close()

def haceInsert():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    #cursor.execute(""" insert into test (campo1,campo2,estado) values ( 'beatriz','gonzalez',0)  """)
    #insert many start
    namedict = ({"campo1":"Joshua", "campo2":"Drake", "estado":"1"},
            {"campo1":"Steven", "campo2":"Foo", "estado":"1"},
            {"campo1":"David", "campo2":"Bar", "estado":"1"})    
    cursor.executemany("""INSERT INTO test(campo1,campo2,estado) VALUES (%(campo1)s, %(campo2)s,%(estado)s)""", namedict)
    #insert many end
    conn.commit()
    conn.close()


def haceUpdate():

    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
#    cursor.execute(""" delete from test where campo1 = 'David'  """)
    cursor.execute(""" update test set estado = 1 where estado = 0  """)
    conn.commit()
    conn.close()
    

def convUTF8(cadena):
    try:
        return str(cadena).replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","Ñ")
    except:
        return cadena


def municipios():
    m = []
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute('select id, municipi_1 from municipios ')
    rows = cursor.fetchall()
 
    for row in rows:
        m.append([row[0],row[1].upper()])
        #print(row[0],row[1])
    conn.close()
    return m


def ejecutaComandoPsql(query):
    try:
        #print(query)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
    except:
        write("error en ejecutar comando psql")


def getProcessDate():
    try:
        from datetime import date
        today = date.today()
        yesterday = today - datetime.timedelta(days=1)
        return yesterday
    except:
        write("error en getProcessDate")


def msgDiarios(fecha):
    query = "select textjson from fase1 where fecha > '" + str(fecha) + " 00:00:00' "
    print(fecha)
    print(query)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        s = convUTF8(row[0]).upper()
        n = searchMunicipios(s)
        ejecutaComandoPsql("insert into sosguate(textjson,municipio) values ('" + row[0] + "','" + str(n) + "') ")
    conn.close()



def searchMunicipios(message):
    retorno = 0
    print(message)
    for n, m in nombreMunicipios:
        #print(n,m)
        if (m in message):
            print(True, m)
            retorno = n
    return retorno


    

fecha = getProcessDate()
nombreMunicipios = municipios()

msgDiarios(fecha)


#print(nombreMunicipios)
#main()
#haceInsert()
#haceUpdate()
#hacequery()

 
