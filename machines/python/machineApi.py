#!/usr/bin/env python
import os,time
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
@app.route(app.config['ROUTE_PATH'] + 'move_right', methods=['GET'])
def right_movement():
    #runForward()
    os.system('nohup python3 /home/pi/python/machines/python/stepperRight.py')
    return (jsonify({'msg':'OK'}))


#METHOD TO CREATE NEW ACCESS IF NEEDED TO THE END POINT
@app.route(app.config['ROUTE_PATH'] + 'move_left', methods=['GET'])
def left_movement():
    os.system('nohup python3 /home/pi/python/machines/python/stepperLeft.py')
    #runBackwards()
    return (jsonify({'msg':'OK'}))


@app.route('/', methods=['GET'])
def start_task():
    data = request.get_json()
    def long_running_task(**kwargs):
        your_params = kwargs.get('post_data', {})
        print("Starting long task")
        print("Your params:", your_params)
        for _ in range(10):
            time.sleep(1)
            print(".")
    thread = threading.Thread(target=long_running_task, kwargs={
                    'post_data': data})
    thread.start()
    return {"message": "Accepted"}, 202




@app.route(app.config['ROUTE_PATH'] + 'Post_data'  ,methods=['POST'])
def rootAddress():
    #hago los reqs
    return jsonify({'msg':'Data Fetched.'})



if __name__ == '__main__':
    print('starting application')
    GPIO.setmode(GPIO.BOARD)
    for o in outs:
    	GPIO.setup(o,GPIO.OUT)

    #if not os.path.exists('db.sqlite'):
    #    db.create_all()
    app.run(host='0.0.0.0', port= app.config['PORT'] )


