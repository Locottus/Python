import os,sys, psycopg2,flask,jsonify,request,json
from flask_cors import CORS
from psycopg2.extras import RealDictCursor

#https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
#https://bitlaunch.io/blog/create-a-bitcoin-node-with-ubuntu/
#nohup pythonScript.py
conn_string = "host='localhost' dbname='swift' user='postgres' password='Guatemala1'"
NETWORK = 'testnet'
#################################### PGADMIN ################################################

  
#https://phoenixnap.com/kb/how-to-connect-postgresql-database-command-line

def recordAddress(data):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    q = """insert into public."addresses" (address,id) values('"""+str(data['address']) +"','""" + str(data['id']) + """')"""
    print(q)
    cursor.execute(q)
    conn.commit()
    conn.close()
    return """{\"msg\":\"""" + str(data['id']) + """ \",\"id\":\"""" + str(data['address']) + "\"}"""
    


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
    w = wallet.create_wallet(network='btctest',seed=None,children=0)#TESTNET
    return w


def createKey(WALLET_PUBKEY,childNumber):
    user_addr = wallet.create_address(network='btctest',xpub=WALLET_PUBKEY,child=int(childNumber))# CREAMOS NUEVAS DIRECCIONES TESTNET
    #rand_addr = wallet.create_address(network="btctest", xpub=WALLET_PUBKEY)
    json = str(user_addr)   
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
pwdRestful = 'b47fcec016832713da3ef91ff64d7d42d3649c830e0964eab51b99ebdb0f88f3037dd43c8a71cad25d3e497be6f355f43b510e8ac59a46389f58eb7fat7fdi3w5s'
usrRestful = 'usrRestful'
#https://blog.miguelgrinberg.com/post/restful-authentication-with-flask

from flask import Flask,request
app = Flask(__name__)
cors = CORS(app, resources={route + '*': {"origins": "*"}})


def addressStatusRequest(address):
    print('address postgres req')
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    q = """select status from public."addresses" where address = '"""+ address + "'"
    cursor.execute(q)
    print(q)
    s = "";
    rows = cursor.fetchall()
    if cursor.rowcount == 0:
        conn.close()
        return """{\"msg\":\"0\",\"id\":\"""" + address + "\"}"""
    else:
        for row in rows:
            s = """{\"msg\":\"""" + str(row[0]) + """ \",\"id\":\"""" + address + "\"}"""
        conn.close()
        return s


def getAddress(id):
    print('address postgres req')
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    q = """select address from public."addresses" where id = '"""+ id + "'"
    cursor.execute(q)
    print(q)
    address = "N/A"
    s = "";
    rows = cursor.fetchall()
    if cursor.rowcount == 0:
        conn.close()
        return """{\"msg\":\"0\",\"id\":\"""" + address + "\"}"""
    else:
        for row in rows:
            s = """{\"msg\":\"""" + id + """ \",\"id\":\"""" + str(row[0]) + "\"}"""
        conn.close()
        return s


@app.route(route + 'addressDestination',methods=['GET'])
def AddressDestination():
    id = request.args.get('id')
    return getAddress(id)


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
def postAddressId():
    data = request.get_json()
    return  recordAddress(data)
    

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


@app.route(route + 'createWallet',methods=['GET'])
def createWallet():
    #request.args.get('id')
    w = wall3()
    privatek = w["private_key"]
    publick = w["public_key"]
    address = w["address"]
    seed = w["seed"]
    coin = w["coin"]
    address3 = address#keyWith3(publick)
    xprivate_key = w["xprivate_key"]
    xpublic_key = w["xpublic_key"]
    xpublic_key_prime = w["xpublic_key_prime"]
    json = '{ "coin":"'+coin+'", ' + '"private_key" : "'+privatek+'", "public_key" :' +'"'+publick+'", ' + '"address" : "'+address+'", "Multi_address" : "'+address3+'", "seed":"' + seed +'", '
    json = json + '"xprivate_key":"'+xprivate_key+'", "xpublic_key" : "' + xpublic_key + '",  "xpublic_key_prime" :' + '"' + xpublic_key_prime + '" }'
    #print(json)
    return json
   
  
if __name__ == '__main__':
    #app.run(debug=True)
    print("starting chat service TESTNET ")
    #app.run(ssl_context='adhoc',host='0.0.0.0', port=1600)
    app.run(host='0.0.0.0', port=1600)
    #recordAddress('mrT4B6R2mSepL3KvWYjXbhYcTUJqxrgCUn','herlich1@gmail.com')
