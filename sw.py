import os,sys, psycopg2,flask,jsonify,request,json
from flask_cors import CORS

#https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/
#https://bitlaunch.io/blog/create-a-bitcoin-node-with-ubuntu/

conn_string = "host='localhost' dbname='swift' user='postgres' password='Guatemala1'"


def getMessages(toMsg):
    from psycopg2.extras import RealDictCursor
    conn = psycopg2.connect(conn_string)
    list = []
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""select msg, tomsg, sent, datetime from public."offlineChat" where tomsg = '"""+ toMsg +"'")
    l = json.dumps(cursor.fetchall(),indent = 2)
    conn.close()
    borrarMensaje(toMsg)
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



from flask import Flask,request
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_tasks():
#    return jsonify({'tasks': tasks})


#http://localhost:5000/api/get?username=herlich&password=pwd1
@app.route('/api/get',methods=['GET'])
def getMsgs():
    id = request.args.get('id')
    #msg = request.args.get('msg')
    print('get messages from: ' + id)
    return getMessages(id)#"""{\"msg\":\"ok\"}"""


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
    grabaMensaje(req_data)
    return """{\"msg\":\"ok\"}"""#requests.status_codes._codes[200]
    



if __name__ == '__main__':
    #app.run(debug=True)
    print("starting chat service")
    app.run(host='localhost', port=1500)
