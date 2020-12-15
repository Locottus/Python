#https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

import os,sys, psycopg2,flask,jsonify,request,json
from flask_cors import CORS

route = r"/api/mobil/"
pwdRestful = 'pwd'#'b47fcec016832713da3ef91ff64d7d42d3649c830e0964eab51b99ebdb0f88f3037dd43c8a71cad25d3e497be6f355f43b510e8ac59a46389f58eb7fat7fdi3w5s'
usrRestful = 'usrRestful'


from flask import Flask,request
app = Flask(__name__)
cors = CORS(app, resources={route + '*': {"origins": "*"}})


@app.route(route + 'get',methods=['GET'])
def getMsgs():
   print('get messages from: ')
   return '{"msg":"ok"}'


if __name__ == '__main__':
    #app.run(debug=True)
    print("starting chat service MAINNET ")
    app.run(ssl_context='adhoc',host='0.0.0.0', port=1700)
    #app.run(host='0.0.0.0', port=1700)
