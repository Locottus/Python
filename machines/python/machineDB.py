import psycopg2
conn_string = "host='192.168.1.13' dbname='Machine' user='postgres' password='Guatemala1'"

def ejecutaComandoPsql(query):
    try:
        print(query)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
    except:
        print("error en ejecutar comando psql")
    #return response.json()

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
        #return response.json()
    conn.close()



