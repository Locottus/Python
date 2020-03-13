import requests,json,psycopg2,time

conn_string = "host='localhost' dbname='iotgis' user='postgres' password='password'"

#https://realpython.com/python-requests/

# ALTER TABLE e1ms1 ADD COLUMN estado numeric default 0;

#**************************************************** database ***************************************************************************
def getSQLData():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    Q = 'select infrasonido_1,infrasonido_2,infrasonido_3,infrasonido_4,audible_1,mpu_rotx,mpu_roty,mpu_rotz,posicion, to_char(fecha_recepcion, \'YYYY-MM-DD HH:MI:SS\') as fecha_recepcion, mpu_gxe, mpu_gye, mpu_gze, mpu_axe, mpu_aye, mpu_aze from e1ms1  ' 
    cursor.execute(Q)# where estado = 0
    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)}   for value in cursor.fetchall()]
    rows = cursor.fetchall()
    #dataStr = str(result).replace("'",'"')
    #print(dataStr)
    conn.close()
    return result


def updateTabla(where):
    query = ' update e1ms1 set estado = 1 where  fecha_recepcion in ( ' + where + ' ) '
    print (query)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def updateStatus(data):
    print('actualizando data')
    s = '';
    for  f in data:
        #print(f['fecha_recepcion'])
        s = s + '\'' + f['fecha_recepcion'] + '\','
    return  s[:-1]

#********************************************** rest ****************************************************************************************


def postMethod(objeto):
    #response = requests.post('https://arcgis-web.url.edu.gt/incyt/api/iot/E1MS1', data=objeto)
    headers = {'content-type': 'application/json'}
    response = requests.post('http://localhost:3001/incyt/api/iot/E1MS1', data = json.dumps(objeto), headers=headers)
    
    #print(response.status_code)
    if response.status_code == 201:
        print('Success!')
    else : #response.status_code == 404:
        print('algo terrible ha ocurrido')
    return response.status_code



def principal():
    data  = getSQLData()
    resp = postMethod(data)
    if resp == 201:
        print('update data')
        updateTabla(updateStatus(data))   


#void main()
print('programa inicia')
while(True):
    principal()
    time.sleep( 60 )#espera de 60 segundos
    print(time.ctime())
