#!/usr/bin/env python
import os,time,jwt
from flask import Flask, abort, request, jsonify, g, url_for
#from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
#from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tokenPaAuthNewUs3rs'
app.config['ROUTE_PATH'] = r"/api/"
app.config['PORT'] = 5000
cors = CORS(app, resources={app.config['ROUTE_PATH'] + '*': {"origins": "*"}})


#METHOD TO CREATE NEW ACCESS IF NEEDED TO THE END POINT
@app.route(app.config['ROUTE_PATH'] + 'post_data', methods=['POST'])
def new_user():
    return (jsonify({'msg':'data Posted.'}))


@app.route(app.config['ROUTE_PATH'] + 'get_data'  ,methods=['GET'])
def rootAddress():
    #hago los reqs
    return jsonify({'msg':'Data Fetched.'})



if __name__ == '__main__':
    print('starting application')
    #if not os.path.exists('db.sqlite'):
    #    db.create_all()
    app.run(host='0.0.0.0', port= app.config['PORT'] )


