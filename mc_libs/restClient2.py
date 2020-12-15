import os,requests,json
import pika


queue = 'hello'
routing_key = 'hello'
mq_host = 'localhost'

#from flask_cors import CORS
#import flask

#https://realpython.com/python-requests/
#https://docs.python.org/3/library/queue.html

#local environment vars.
'''
base_url = os.environ['HealthJumpURL']
email = os.environ['HealthJumpEmail']
password = os.environ['HealthJumpPassword']
SecretKey = os.environ['HealthJumpSecretKey']
Version = os.environ['HealthJumpVersion']
ClientID = os.environ['HealthJumpClientID']
routePath = os.environ['HealthJumpServerPath']
apiPort = os.environ['HealthJumpServerApiPort']
'''


#DEV vars for reference when setting env.
base_url = 'https://api.healthjump.com/hjdw/'
email ='sandbox@healthjump.com'
password = 'R-%Sx?qP%+RN69CS'
SecretKey = 'yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g'
Version = '3.0'

ClientID = 'SBOX02'
routePath = r"/api/"
apiPort = 1600

def getClients(token,parm=None):
    print('getClients')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    
    url = base_url + ClientID + '/client_ids'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
       
    else : 
        print('error')
        print(json.loads(response.content))

    return response.json()# json.loads(response.content)






def getAllergies(token,parm=None):
    print('getClients')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/allergy'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
       
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getAppointments(token,parm=None):
    print('getAppointments')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/appointment'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
       
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        #print(json.loads(response.content))
        print(response.json)
        #return response.json
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)



def getAttribution(token,parm=None):
    print('getAttribution')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/attribution'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)



def getCharge(token,parm=None):
    print('getCharge')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    url = base_url + ClientID + '/charge'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)
'''
def getChargeWParms(token,parm=None):
    #?hj_modify_timestamp=btwn~2016-10-08 01:54:43.956800~2016-10-13 20:54:43.956820
    print('getChargeWParms')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

   
    response = requests.get('https://api.healthjump.com/hjdw/' + ClientID + '/charge?' + parm,headers = headers)
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))

'''


def getDemographics(token,parm=None):
    print('getDemographics')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/demographic'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)

def getDiagnosis(token,parm=None):
    print('getDiagnosis')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    url = base_url + ClientID + '/diagnosis'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getEncounters(token,parm=None):
    print('getEncounters')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    
    url = base_url + ClientID + '/encounter'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getInmunization(token,parm=None):
    print('getInmunization')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    
    url = base_url + ClientID + '/immunization'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)

def getLabOrder(token,parm=None):
    print('getLabOrder')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    
    url = base_url + ClientID + '/lab_order'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getLabResult(token,parm=None):
    print('getLabResult')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/lab_result'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getMedication(token,parm=None):
    print('getMedication')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    
    url = base_url + ClientID + '/medication'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getPayers(token,parm=None):
    print('getPayers')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/payer_dim'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getProcedures(token,parm=None):
    print('getProcedures')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/procedure'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getProviders(token,parm=None):
    print('getProviders')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/provider'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)

def getSocialHistory(token,parm=None):
    print('getSocialHistory')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/social_history' 
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getTransactions(token,parm=None):
    print('getTransactions')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    

    url = base_url + ClientID + '/transaction'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)


    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getVitals(token,parm=None):
    print('getVitals')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }

    url = base_url + ClientID + '/vitals'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    
    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)


def getUnload(token,parm=None):
    print('getUnload')
    headers={"Secretkey" : SecretKey,
             "Version":Version,
             "Authorization":"Bearer " + token 
             }
    
    url = base_url + ClientID + '/appointment'
    if parm is not None:
        url += '?' + parm    
        
    response = requests.get(url,headers = headers)

    
    print(response)
    print(response.headers)
    #print(response.json())  #esta es la respuesta en json

    if response.status_code == 200:
        print('Success!')
        print(json.loads(response.content))
        
    else : 
        print('error')
        print(json.loads(response.content))
    return response.json()# json.loads(response.content)





#first step before request to an endpoint
def postAuthenticate():
    print('asking for new token')
    body = ({"email": email, "password": password})
    response = requests.post('https://api.healthjump.com/authenticate', data=body)
    #print(response.content)
    token = json.loads(response.content)
    print(token['token'])
    #print(response.status_code)
    if response.status_code == 200:
        print('Success!')
        return token['token']
    else : #error
        return ""

def sendMessageToMQ(body):
    print('sending to mq')
    connection = pika.BlockingConnection( pika.ConnectionParameters(host= mq_host ))
    channel = connection.channel()
    channel.queue_declare(queue= queue)
    channel.basic_publish(exchange='', routing_key= routing_key , body= body)
    #print(" [x] Sent 'Hello World !'")
    connection.close()


def getAllData():
    print('getting all data')
    token = postAuthenticate()

    #clients = getClients(token)
    allergies = getAllergies(token)
    appointments = getAppointments(token)
    attributions = getAttribution(token)

    allData = {
        "allergies" : allergies,
        "appointments" : appointments,
        "atrributions" : attributions,
        }

    #print(allData)
    return str(allData)


#SERVICES REST
'''    
from flask import Flask,request
app = Flask(__name__)
cors = CORS(app, resources={routePath + '*': {"origins": "*"}})


@app.route(routePath  ,methods=['GET'])
def rootAddress():
    token = postAuthenticate()
    #hago los reqs
    return getAllergies(token)

'''



if __name__ == '__main__':
    #app.run(debug=True)
    print("starting")
    import ast
    datos = ast.literal_eval(getAllData())
    d = datos["allergies"]
    print('***************************************')
    print(d)

    print('***************************************')
    d = datos["appointments"]
    print(d)

    
    #sendMessageToMQ(datos)
    #app.run(ssl_context='adhoc',host='0.0.0.0', port=apiPort)
    #app.run(host='0.0.0.0', port=apiPort)

    
    #token = postAuthenticate()
    #getAppointments(token,"provider_id=1234564502")
    #getAppointments(token)
    #getAllergies(token)
