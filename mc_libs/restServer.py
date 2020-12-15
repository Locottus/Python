import os,sys, psycopg2,flask,jsonify,request,json
from flask_cors import CORS


from flask import Flask,request
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


#http://localhost:5000/api/get?username=herlich&password=pwd1
@app.route('/api/get',methods=['GET'])
def getMsgs():
    return """{\"msg\":\"ok\"}"""



#http://localhost:5000/api/post
@app.route('/api/post',methods=['POST'])
def postMsg():
    print('posting message')
    return """{\"msg\":\"ok\"}"""
    


if __name__ == '__main__':
    #app.run(debug=True)
    print("starting chat service")
    #app.run(ssl_context='adhoc',host='0.0.0.0', port=1500)
    app.run(host='0.0.0.0', port=1500)

