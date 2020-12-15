import os,requests,json
import pika
import psycopg2

from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker


'''

#variables de entorno

RABBIT_HOST="3.235.107.32"
RABBIT_USER="admin"
RABBIT_PWD="RQDpTAKGh8eD88fh"
HealthJump_base_url="https://api.healthjump.com/hjdw/"
HealthJumpEmail="sandbox@healthjump.com"
HealthJumpPassword="R-%Sx?qP%+RN69CS"
HealthJumpSecretKey="yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g"
HealthJumpVersion="3.0"
healthJump_db_string="postgres://postgres:Guatemala1@localhost:5432/healthjump"




#DEV vars for reference when setting env.
db_string = "postgres://postgres:Guatemala1@localhost:5432/healthjump"
base_url = 'https://api.healthjump.com/hjdw/'
email ='sandbox@healthjump.com'
password = 'R-%Sx?qP%+RN69CS'
SecretKey = 'yemj6bz8sskxi7wl4r2zk0ao77b2wdpvrceyoe6g'
Version = '3.0'
'''

base_url = os.environ['HealthJump_base_url']
email = os.environ['HealthJumpEmail']
password = os.environ['HealthJumpPassword']
SecretKey = os.environ['HealthJumpSecretKey']
Version = os.environ['HealthJumpVersion']
db_string = os.environ['healthJump_db_string']
RABBIT_HOST = os.environ['RABBIT_HOST']
RABBIT_USER = os.environ['RABBIT_USER']
RABBIT_PWD = os.environ['RABBIT_PWD']


#ClientID = 'SBOX02'
#routePath = r"/api/"
#apiPort = 1600

def getClients(token,ClientID,parm=None):
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






def getAllergies(token,ClientID,parm=None):
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


def getAppointments(token,ClientID,parm=None):
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



def getAttribution(token,ClientID,parm=None):
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



def getCharge(token,ClientID,parm=None):
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


def getDemographics(token,ClientID,parm=None):
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

def getDiagnosis(token,ClientID,parm=None):
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


def getEncounters(token,ClientID,parm=None):
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


def getInmunization(token,ClientID,parm=None):
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

def getLabOrder(token,ClientID,parm=None):
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


def getLabResult(token,ClientID,parm=None):
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


def getMedication(token,ClientID,parm=None):
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


def getPayers(token,ClientID,parm=None):
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


def getProcedures(token,ClientID,parm=None):
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


def getProviders(token,ClientID,parm=None):
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

def getSocialHistory(token,ClientID,parm=None):
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


def getTransactions(token,ClientID,parm=None):
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


def getVitals(token,ClientID,parm=None):
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


def getUnload(token,ClientID,parm=None):
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
    credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PWD)
    parameters = pika.ConnectionParameters(credentials=credentials, host=RABBIT_HOST)
    print('sending')
    connection = pika.BlockingConnection(parameters)  # Establishes TCP Connection with RabbitMQ
    channel = connection.channel()  # Establishes logical channel within Connection

    channel.basic_publish(exchange='', routing_key='HealthJump', body=str(body))  # Send Message
    connection.close()
    print('data sent')


def getAllData(ClientID):
    print('getting all data')
    token = postAuthenticate()

    #clients = getClients(token)
    allergies = getAllergies(token,ClientID)
    appointments = getAppointments(token,ClientID)
    attributions = getAttribution(token,ClientID)
    charge = getCharge(token,ClientID)
    demographics = getDemographics(token,ClientID)
    diagnonsis = getDiagnosis(token,ClientID)
    encounters = getEncounters(token,ClientID)
    inmunization = getInmunization(token,ClientID)
    laborder = getLabOrder(token,ClientID)
    labresult = getLabResult(token,ClientID)
    medication = getMedication(token,ClientID)
    payers = getPayers(token,ClientID)
    procedures = getProcedures(token,ClientID)
    providers = getProviders(token,ClientID)
    history = getSocialHistory(token,ClientID)
    transactions = getTransactions(token,ClientID)
    vitals = getVitals(token,ClientID)
    unload = getUnload(token,ClientID)

    allData = {
        "clientId": ClientID,
        "allergies" : allergies,
        "appointments" : appointments,
        "atrributions" : attributions,
        "charge" : charge,
        "demographics": demographics,
        "diagnonsis" : diagnonsis,
        "encounters": encounters,
        "inmunization" : inmunization,
        "laborder" : laborder,
        "labresult" : labresult,
        "medication" : medication,
        "payers" : payers,
        "procedures" : procedures,
        "providers" : providers,
        "history" : history,
        "transactions" : transactions,
        "vitals" : vitals,
        "unload" : unload
        }

    #print(allData)
    return allData



db = create_engine(db_string)  
base = declarative_base()

class Client(base):  
    __tablename__ = 'table_clients_test'
    client = Column(String, primary_key=True)
   
Session = sessionmaker(db)  
session = Session()
base.metadata.create_all(db)

# Create test client
#test_client = Client(client="SBOX02")  
#session.add(test_client)  
#session.commit()



def getAllClientsData():
    conn = psycopg2.connect(db_string)
    cursor = conn.cursor()
    cursor.execute("select client from table_clients_test")
    rows = cursor.fetchall()
 
    for row in rows:
        datos = getAllData(row[0])    
        sendMessageToMQ(datos)
    conn.close()



if __name__ == '__main__':
    print("starting")
    getAllClientsData()    
