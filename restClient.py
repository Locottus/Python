import requests,json
#https://realpython.com/python-requests/



def getMethod():
    response = requests.get('https://arcgis-web.url.edu.gt/incyt/api/mensajes')
    if response.status_code == 200:
        print('Success!')
        #print(response.headers)
        print(response.json())  #esta es la respuesta en json
    else : #response.status_code == 404:
        print('algo terrible ha ocurrido')


def getMethodParametros():
    response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},)
    if response.status_code == 200:
        print('Success!')
        #print(response.headers)
        print(response.json())  #esta es la respuesta en json
    else : #response.status_code == 404:
        print('algo terrible ha ocurrido')



def postMethod(objeto):
    response = requests.post('https://arcgis-web.url.edu.gt/incyt/api/mensaje', data=objeto)
    print(response.status_code)
    if response.status_code == 201:
        print('Success!')
    else : #response.status_code == 404:
        print('algo terrible ha ocurrido')

def postFileMethod(rutaArchivo):
    #'c:\german.jpg' -->rutaArchivo ejemplo
    url = 'https://arcgis-web.url.edu.gt/incyt/api/HashFiles/postFile'
    files = {'file': open(rutaArchivo,'rb')}
    response = requests.post(url, files=files)
    print(response.status_code)
    print(response.text)
    if response.status_code == 201:
        print('Success!')
    else : #response.status_code == 404:
        print('algo terrible ha ocurrido')



#void main()
print('programa inicia')
obj = [
    {
        "id": 3,
        "infrasonido_1": 100,
        "infrasonido_2": 200,
        "infrasonido_3": 300,
        "infrasonido_4": 400,
        "audible_1": 500,
        "mpu_rotx": 5070,
        "mpu_roty": 5008,
        "mpu_rotz": 5009,
        "posicion": "-90.15,14.445",
        "fecha_recepcion": "2020-03-03T03:49:47.741Z",
        "mpu_gxe": 50011,
        "mpu_gye": 5002,
        "mpu_gze": 5003,
        "mpu_axe": 5004,
        "mpu_aye": 5005,
        "mpu_aze": 5006
    },
    {
        "id": 4,
        "infrasonido_1": 2100,
        "infrasonido_2": 2200,
        "infrasonido_3": 3300,
        "infrasonido_4": 4400,
        "audible_1": 5005,
        "mpu_rotx": 507760,
        "mpu_roty": 50078,
        "mpu_rotz": 500669,
        "posicion": "-90.55515,14.445",
        "fecha_recepcion": "2020-03-03T03:49:47.741Z",
        "mpu_gxe": 501011,
        "mpu_gye": 5065562,
        "mpu_gze": 500653,
        "mpu_axe": 500654,
        "mpu_aye": 500565,
        "mpu_aze": 505506
    }
]



postFileMethod()
'''
#esto convierte un string a un json:
#objJson = json.loads(objStr)
print(obj)
#esto te da el tamano del objeto
print(len(obj))
#para acceder a diferentes elementos del arreglo de objetos json -->puede ser recorrido con un while
print (obj[0]['infrasonido_1'])
print (obj[1]['posicion'])

contador = 0;
while (contador < (len(obj))):
    for key, value in obj[contador].items():
        print (str(key) + ' ' + str(value))
    contador = contador + 1
    print('')
'''
