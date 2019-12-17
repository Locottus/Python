import os,sys, psycopg2,flask,jsonify,request,json
from flask_cors import CORS
from psycopg2.extras import RealDictCursor

#https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
#https://bitlaunch.io/blog/create-a-bitcoin-node-with-ubuntu/
#nohup pythonScript.py
conn_string = "host='localhost' dbname='swift' user='postgres' password='Guatemala1'"
NETWORK = 'mainnet'
#################################### PGADMIN ################################################

  
#https://phoenixnap.com/kb/how-to-connect-postgresql-database-command-line

def recordAddress(address,amount):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    q = """insert into public."addresses" (address,status,datetime,amount) values('"""+str(address) +"','1',now(),'""" + str(amount) + "')"
    print(q)
    cursor.execute(q)
    conn.commit()
    conn.close()
    return addressStatusRequest(address)


def getMessages(toMsg):
    conn = psycopg2.connect(conn_string)
    list = []
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""select msg from public."offlineChat" where tomsg = '"""+ toMsg +"'")
    conn.close()
    l = json.dumps(cursor.fetchall(),indent = 2)
    return l

def grabaMensaje(data):
    msg = str(data)#str(data['msg'])
    tomsg = str(data['tomsg'])
    sent = str(data['sent'])
    datetime = str(data['datetime'])
    
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print(msg + " " + tomsg + " " + str(sent) + " " + datetime)
    #query = """ insert into public."offlineChat" (msg,tomsg,sent,datetime) values ( '""" + data +"','" + tomsg +"'," + sent + ",'" +  datetime + "')"
    q = """insert into public."offlineChat" (msg,tomsg,sent,datetime) values('"""+  msg.replace("'", "\"") +"','"+ tomsg +"','"+sent+"','" +datetime +"')"
    #print(q)
    cursor.execute(q)
    conn.commit()
    conn.close()

def borrarMensaje(tomsg):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    q = """ delete from public."offlineChat" where tomsg = '"""+ tomsg +"' "
    #print(q)
    cursor.execute(q)
    conn.commit()
    conn.close()

########################################## BTC ##########################################################
from bitcoin import *
from pywallet import wallet


def keyWith3(my_public_key1):
    #my_public_key1 = privtopub(pKey)
    #print('Public Key 1: ' + my_public_key1)
    my_multi_sig = mk_multisig_script(my_public_key1, my_public_key1, my_public_key1, 2,3)
    my_multi_address = scriptaddr(my_multi_sig)
    #print('Multi-Address: ' + my_multi_address)
    return my_multi_address


#https://github.com/ranaroussi/pywallet
def wall3():
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()
    # create bitcoin wallet
    w = wallet.create_wallet(network='BTC',seed=None,children=0)#TESTNET
    return w


def createKey(WALLET_PUBKEY,childNumber):
    user_addr = wallet.create_address(network='BTC',xpub=WALLET_PUBKEY,child=int(childNumber))# CREAMOS NUEVAS DIRECCIONES TESTNET
    #rand_addr = wallet.create_address(network="btctest", xpub=WALLET_PUBKEY)
    json =  str(user_addr) 
    #print(json)
    return json

def newKeyWith3(my_public_key1):
    my_public_key2 = privtopub(random_key())

    print(my_public_key1)
    print(my_public_key2)
    #print(my_public_key3)
    my_multi_sig = mk_multisig_script(my_public_key1, my_public_key1, my_public_key2, 2,3)
    my_multi_address = scriptaddr(my_multi_sig)
    #print('Multi-Address: ' + my_multi_address)
    return my_multi_address


#https://community.microstrategy.com/s/article/Sample-REST-API-in-Python-Authentication?language=en_US
##################################### SERVICES ################################################################
route = r"/api/mobil/"
pwdRestful = 'pwd'#'b47fcec016832713da3ef91ff64d7d42d3649c830e0964eab51b99ebdb0f88f3037dd43c8a71cad25d3e497be6f355f43b510e8ac59a46389f58eb7fat7fdi3w5s'
usrRestful = 'usrRestful'
#https://blog.miguelgrinberg.com/post/restful-authentication-with-flask

from flask import Flask,request
app = Flask(__name__)
cors = CORS(app, resources={route + '*': {"origins": "*"}})

def checkCredentials(usr, pwd):
    if usr == usrRestful and pwd == pwdRestful:
        return True
    else:
        return False

def errorMsg():
    return  abort(400)#"""{\"msg\":\"error\"}"""

def okMsg():
    return """{\"msg\":\"ok\"}"""

def addressStatusRequest(address):
    print('address postgres req')
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    q = """select status from public."addresses" where address = '"""+ address +"'"
    cursor.execute(q)
    print(q)
    s = "";
    rows = cursor.fetchall()
    if cursor.rowcount == 0:
        conn.close()
        return """{\"status\":\"0\"}"""
    else:
        for row in rows:
            s = """{\"status\":\"""" + str(row[0]) + """\"}"""
        conn.close()
        return s

@app.route(route + 'newAddress',methods=['GET'])
def newAddress():
    key = request.args.get('key')
    child = request.args.get('child')
    return createKey(key,child)


@app.route(route + 'addressStatus',methods=['GET'])
def addressStatus():
    address = request.args.get('address')
    print(address)
    return addressStatusRequest(address)

@app.route(route + 'postAddress',methods=['POST'])
def postAddress():
    address = request.args.get('address')
    amount = request.args.get('amount')
    return recordAddress(address,amount)
    

@app.route(route + 'getNewTransaction',methods=['GET'])
def createNewChildWallet2():
    #request.args.get('id')
    publicKey = request.args.get('publicKey')
    publicChildNum = request.args.get('publicChildNum')
    print(publicKey)
    print(publicChildNum)
    return createKey(publicKey,publicChildNum)


@app.route(route + 'getNewChild',methods=['GET'])
def createNewChildWallet():
   publicKey = request.args.get('publicKey')
   publicChildNum = request.args.get('publicChildNum')
   print(publicKey)
   print(publicChildNum)
   return createKey(publicKey,publicChildNum)


#http://localhost:1500/api/createWallet?id=herlich@gmail.com
@app.route(route + 'createWallet',methods=['GET'])
def createWallet():
    print('va por create wallet')
    #request.args.get('id')
    w = wall3()
    privatek = w["private_key"]
    publick = w["public_key"]
    address = w["address"]
    seed = w["seed"]
    coin = w["coin"]
    address3 = keyWith3(publick)
    xprivate_key = w["xprivate_key"]
    xpublic_key = w["xpublic_key"]
    xpublic_key_prime = w["xpublic_key_prime"]
    json = '{ "coin":"'+coin+'", ' + '"private_key" : "'+privatek+'", "public_key" :' +'"'+publick+'", ' + '"address" : "'+address+'", "Multi_address" : "'+address3+'", "seed":"' + seed +'", '
    json = json + '"xprivate_key":"'+xprivate_key+'", "xpublic_key" : "' + xpublic_key + '",  "xpublic_key_prime" :' + '"' + xpublic_key_prime + '" }'
    print(json)
    return json
   


@app.route(route + 'get',methods=['GET'])
def getMsgs():
   print('get messages from: ' + id)
   return getMessages(id)



@app.route(route + 'post',methods=['POST'])
def postMsg():
    print('posting message')
    req_data = request.get_json()
    print(req_data)
    return """{\"msg\":\"ok\"}"""#requests.status_codes._codes[200]
    

if __name__ == '__main__':
    #app.run(debug=True)
    print("starting chat service MAINNET ")
    #app.run(ssl_context='adhoc',host='0.0.0.0', port=1700)
    app.run(host='0.0.0.0', port=1700)
    #createKey('tpubD6NzVbkrYhZ4X3ytjTHoSnmHsUdgXiBTm4LQh6FXXGi7uqRVmvR4h8poyTbnxXrDm9xhpqV8ioTJ884wQ7mvaDZCBvsYRa1fCMSJrW7U1Bp',2)
