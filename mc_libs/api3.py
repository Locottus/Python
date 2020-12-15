#!/usr/bin/env python
import os,time,jwt
from flask import Flask, abort, request, jsonify, g, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tokenPaAuthNewUs3rs'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['ROUTE_PATH'] = r"/api/"
app.config['PORT'] = 5000
cors = CORS(app, resources={app.config['ROUTE_PATH'] + '*': {"origins": "*"}})


# extensions
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id, 'exp': time.time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],
                              algorithms=['HS256'])
        except:
            return
        return User.query.get(data['id'])


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


#METHOD TO CREATE NEW ACCESS IF NEEDED TO THE END POINT
@app.route(app.config['ROUTE_PATH'] + 'new_user', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    secret = request.json.get('secret')
    #print(username,password,secret)

    if (secret != app.config['SECRET_KEY']):
        abort(400)      #no secret key given
    if username is None or password is None:
        abort(400)    # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400)    # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return (jsonify({'msg':'New user successfully created.'}))




#TODO PLACE HERE THE METHOD TO RETURN THE REAL DATA
@app.route(app.config['ROUTE_PATH'] + 'patient_data')
@auth.login_required
def get_resource():
    return jsonify({'msg': 'all works!!!, %s!' % g.user.username})


if __name__ == '__main__':
    print('starting application')
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(host='0.0.0.0', port= app.config['PORT'] )
