import requests
#https://realpython.com/python-requests/


def getMethod():
    response = requests.get('http://arcgis-web.url.edu.gt/incyt/api/mensajes')
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



def postMethod():
    response = requests.post('http://arcgis-web.url.edu.gt/incyt/api/mensaje', data={
        "id": 1,
        "nombre": "steven",
        "telefono": "12345678",
        "email": "noreplay@gmail.com",
        "mensaje": "hola, esta es una prueba post desde python",
        "fechacreacion": "2020-03-02T20:33:04.777Z"
        })
    print(response.status_code)
    if response.status_code == 201:
        print('Success!')
    else : #response.status_code == 404:
        print('algo terrible ha ocurrido')




#void main()
print('programa inicia')
getMethod()
#getMethodParametros()
#postMethod()
