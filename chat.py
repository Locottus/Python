import os,sys, psycopg2,flask,jsonify,request,json
from flask_cors import CORS

conn_string = "host='localhost' dbname='swift' user='postgres' password='Guatemala1'"
route = r"/api/mobil/"


def getMessages_old(toMsg):
    from psycopg2.extras import RealDictCursor
    conn = psycopg2.connect(conn_string)
    list = []
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("""select msg from public."offlineChat" where tomsg = '"""+ toMsg +"'")
    l = json.dumps(cursor.fetchall(),indent = 2)
    conn.close()
    borrarMensaje(toMsg)
    return l

def getMessages(toMsg):
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("""select msg from public."offlineChat" where tomsg = '"""+ toMsg +"'")
    rows = cursor.fetchall()
    #list = []
    s = "[ "
    for row in rows:
        s = s + row[0] + ","
    conn.close()
    ret = s[:-1] + " ]"
    #print (ret)
    borrarMensaje(toMsg)
    return ret 


def grabaMensaje(data):
    dataStr = str(data).replace("'",'"')
    #print(dataStr)
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        q = """insert into public."offlineChat" (msg,tomsg,sent,datetime) values('"""+  dataStr +"','"+ data['to'] +"',False,'" + data['dateTime'] +"')"
        print(q)
        cursor.execute(q)
        conn.commit()
        conn.close()
        return """{\"id\":\""""+ str(data['id']) +"""\",\"msg\":\"ok\"}"""
    except:
        return """{\"id\":\""""+ str(data['id']) +"""\",\"msg\":\"error\"}"""

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


@app.route(route + 'getMessages',methods=['GET'])
def getMsgs():
    id = request.args.get('id')
    #msg = request.args.get('msg')
    #print('get messages from: ' + id)
    return getMessages(id)



@app.route(route + 'postMessages',methods=['POST'])
def postMsg():
    data = request.get_json()
    return grabaMensaje(data)


if __name__ == '__main__':
    #app.run(debug=True)
    print("starting chat service port 1500")
    #app.run(ssl_context='adhoc',host='0.0.0.0', port=1500)
    app.run(host='0.0.0.0', port=1500)
