import os,sys, psycopg2

conn_string = "host='dogmail.cloudapp.net' dbname='dmswitch' user='postgres' password='password'"


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
        print rString
        #print "   ", row[0],row[1],row[2]
    conn.close()

def haceInsert():
    print "hacer el insert"
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
    print "hace el update"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
#    cursor.execute(""" delete from test where campo1 = 'David'  """)
    cursor.execute(""" update test set estado = 1 where estado = 0  """)
    conn.commit()
    conn.close()
    

#main()
#haceInsert()
#haceUpdate()
hacequery()

 
