import os,sys, psycopg2,flask,jsonify,request,json
from flask_cors import CORS


conn_string = "host='localhost' dbname='swift' user='postgres' password='pwd111'"
NETWORK = 'testnet'

def getMessages(toMsg):
    from psycopg2.extras import RealDictCursor
    conn = psycopg2.connect(conn_string)
    list = []
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""select msg from public."offlineChat" where tomsg = '"""+ toMsg +"'")
    l = json.dumps(cursor.fetchall(),indent = 2)
    conn.close()
    #borrarMensaje(toMsg)
    return l

def grabaMensaje(data):
    #print(data)
    #print(data['msg'])
    #print(data['tomsg'])
    #print(data['sent'])
    #print(data['datetime'])
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




def wall3():
    # create_btc_wallet.py
    from pywallet import wallet
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()
    # create bitcoin wallet
    w = wallet.create_wallet(network="BTC", seed=seed, children=1)
    #print(w)
    #print(w["private_key"])
    return str(w)


def createKey(WALLET_PUBKEY,childNumber):
    from pywallet import wallet
    #WALLET_PUBKEY = 'YOUR WALLET XPUB'
    # generate address for specific user (id = 10)
    print(WALLET_PUBKEY)
    print(childNumber)
    user_addr = wallet.create_address(network="BTC", xpub=WALLET_PUBKEY, child=int(childNumber))
    # or generate a random address, based on timestamp
    rand_addr = wallet.create_address(network="BTC", xpub=WALLET_PUBKEY)
    json = "[ " + str(user_addr) + " , " + str(rand_addr) + " ]"  
    #print("User Address\n", user_addr)
    #print("Random Address\n", rand_addr)
    print(json)
    return json

from flask import Flask,request
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route('/api/getNewChild',methods=['GET'])
def createNewChildWallet():
    publicKey = request.args.get('publicKey')
    publicChildNum = request.args.get('publicChildNum')
    print(publicKey)
    print(publicChildNum)
    return createKey(publicKey,publicChildNum)


#http://localhost:1500/api/createWallet?id=herlich@gmail.com
@app.route('/api/createWallet',methods=['GET'])
def createWallet():
    id = request.args.get('id')
    #msg = request.args.get('msg')
    print('get messages from: ' + id)
    return wall3()



#http://localhost:5000/api/get?username=herlich&password=pwd1
@app.route('/api/get',methods=['GET'])
def getMsgs():
    id = request.args.get('id')
    #msg = request.args.get('msg')
    print('get messages from: ' + id)
    return getMessages(id)#"""{\"msg\":\"ok\"}"""
    #return """{\"msg\":\"ok\"}"""


#http://localhost:5000/api/get
@app.route('/api/getJ',methods=['GET'])
def getMsgsJ():
    req_data = request.get_json()
    msg = req_data['msg']
    #username = "herlich"
    print(msg)
    return """{\"msg\":\"ok\"}"""


#http://localhost:5000/api/post
@app.route('/api/post',methods=['POST'])
def postMsg():
    print('posting message')
    req_data = request.get_json()
    print(req_data)
    #grabaMensaje(req_data)
    return """{\"msg\":\"ok\"}"""#requests.status_codes._codes[200]
    



if __name__ == '__main__':
    #app.run(debug=True)
    print("starting chat service")
    #app.run(ssl_context='adhoc',host='0.0.0.0', port=1500)
    app.run(host='0.0.0.0', port=1500)

