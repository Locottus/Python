import os,sys,psycopg2
#from bitcoinlib.wallets import HDWallet
import qrcode

#conn_string = "host='dogmail.cloudapp.net' dbname='dmswitch' user='postgres' password='password'"
conn_string = "host='localhost' dbname='bitchat' user='postgres' password='Guatemala1'"

#esta parte del codigo ya genera qrs solo es de parametrizar y guardar en bd
#https://pypi.org/project/qrcode/
#https://help.ubuntu.com/community/PostgreSQL
def qrGen():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('34mRNWqn9oiQaiDfAJZFpPu9BwNRFGGpWN')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('imgWallet.png')


def haceInsert():
    print ("hacer el insert")
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
    print ("hace el update")
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
#    cursor.execute(""" delete from test where campo1 = 'David'  """)
    cursor.execute(""" update test set estado = 1 where estado = 0  """)
    conn.commit()
    conn.close()


    
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
        print (rString)
        #print "   ", row[0],row[1],row[2]
    conn.close()



#main()
print('inicia porograma')
qrGen()

#https://pypi.org/project/pywallet/








#herlichBTC = HDWallet.create('a', witness_type='p2sh-segwit')
#herlichBTC.get_key().address
#herlichBTC.info()



#https://pypi.org/project/qrcode/
#https://pypi.org/project/PyQRCode/
#https://pypi.org/project/bitcoinlib/
'''
CREATE TABLE public.login
(
    
    login text  NOT NULL,
    password text NULL,
    wallet text NULL,
    private text NULL,
    public text NULL,
    signature text NULL,
    qrWallet bytea NULL,
    qrWalletPrivate bytea NULL,
    qrWalletPublic bytea NULL,
    qrWalletSignature bytea NULL,
    "activeUser" boolean,
    telephone text null,
    CONSTRAINT login_pkey PRIMARY KEY (login)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.login
    OWNER to postgres;



'''
