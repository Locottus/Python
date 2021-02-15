import RPi.GPIO as GPIO
import time 
from array import *

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

#seteo de pines
GPIO.setmode(GPIO.BOARD)
for o in outs:
    GPIO.setup(o,GPIO.OUT)

def wakeupMotor():
    for o in outs:
        GPIO.output(o,GPIO.HIGH)

def sleepMotor():
    for o in outs:
        GPIO.output(o,GPIO.LOW)


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


#void main()
print('starting stepper')


for x in range(500):
    runBackwards()
    print(x)


sleepMotor()
GPIO.cleanup()


