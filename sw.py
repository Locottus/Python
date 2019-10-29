import os,sys, psycopg2,flask,jsonify,request

#https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/

conn_string = "host='localhost' dbname='swift' user='postgres' password='Guatemala1'"


def hacequery(toMsg):
    conn = psycopg2.connect(conn_string)
    list = []
    cursor = conn.cursor()
    cursor.execute("""select * from public."offlineChat" where tomsg = '"""+ toMsg +"'")
    rows = cursor.fetchall()
    rString = ""
    for row in rows:
        rString = "{\"msg\":\"" + row[0] +"\",\"tomsg\":\"" + row[1] +"\",\"sent\":\"" + str(row[2]) + "\",\"datetime\":\"" + str(row[3]) +"\"}"
        list.append(rString)
        print (rString)
    conn.close()
    return list




from flask import Flask,request

app = Flask(__name__)


#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_tasks():
#    return jsonify({'tasks': tasks})

#http://localhost:5000/api/get?username=herlich&password=pwd1
@app.route('/api/get',methods=['GET'])
def getMsgs():
    #username = request.args.get('username')
    #password = request.args.get('password')
    id = request.args.get('id')
    #msg = request.args.get('msg')
    print(username +  " " + password)
    #username = "herlich"
    return """{\"msg\":\"ok\"}"""


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
    print('posting')
    req_data = request.get_json()
    msg = req_data['msg']
    #hacequery("herlich@gmail.com")
    print(msg)
    return """{\"msg\":\"ok\"}"""#requests.status_codes._codes[200]
    



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='localhost', port=5000)
#    hacequery("herlich@gmail.com")
