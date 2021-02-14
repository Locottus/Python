#!/usr/bin/env python
import os,time
from flask import Flask, abort, request, jsonify, g, url_for
#from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
#from werkzeug.security import generate_password_hash, check_password_hash

import RPi.GPIO as GPIO
import time 
from array import *
import logging
import threading

#configuracoin de pines del stepper bipolar
out1 = 11
out2 = 13
out3 = 15
out4 = 16

#delay value
timeValue = 0.005

#matriz de pines del stepper
outs = [out1,out2,out3,out4]

#secuencia para mover el stepper
matriz = [
    [1,0,0,1],
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],

    ]

def setMatrizPins(pin,valor):
    if (valor == 0):
        GPIO.output(outs[pin],GPIO.LOW)
    if (valor == 1):
        GPIO.output(outs[pin],GPIO.HIGH)


def runForward():
    i = 0
    while (i < 4):
        #print(matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3])
        setMatrizPins(0,matriz[i][0])
        setMatrizPins(1,matriz[i][1])
        setMatrizPins(2,matriz[i][2])
        setMatrizPins(3,matriz[i][3])        
        i = i + 1
        time.sleep(timeValue)
           
def runBackwards():
    i = 3
    while (i >=0):
        #print(matriz[i][0],matriz[i][1],matriz[i][2],matriz[i][3])
        setMatrizPins(0,matriz[i][0])
        setMatrizPins(1,matriz[i][1])
        setMatrizPins(2,matriz[i][2])
        setMatrizPins(3,matriz[i][3])        
        i = i - 1
        time.sleep(timeValue)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tokenPaAuthNewUs3rs'
app.config['ROUTE_PATH'] = r"/api/"
app.config['PORT'] = 5000
cors = CORS(app, resources={app.config['ROUTE_PATH'] + '*': {"origins": "*"}})


#METHOD TO CREATE NEW ACCESS IF NEEDED TO THE END POINT
@app.route(app.config['ROUTE_PATH'] + 'move_right', methods=['GET'])
def right_movement():
    #runForward()
    return (jsonify({'msg':'OK'}))


#METHOD TO CREATE NEW ACCESS IF NEEDED TO THE END POINT
@app.route(app.config['ROUTE_PATH'] + 'move_left', methods=['GET'])
def left_movement():
    os.system('nohup python3 /home/pi/python/machines/python/stepper.py')
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


