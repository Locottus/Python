import os,sys, psycopg2,flask,jsonify

conn_string = "host='dogmail.cloudapp.net' dbname='dmswitch' user='postgres' password='password'"


def hacequery():
    #print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)
    #get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    cursor.execute("""select * from test where campo2 = 'gonzalez'""")
    rows = cursor.fetchall()
    rString = ""
    for row in rows:
        rString = "{\"name\":\"" + row[0] +"\",\"lastname\":\"" + row[1] +"\",\"status\":\"" + str(row[2]) + "\"}, "  + rString
        #print rString
        #print "   ", row[0],row[1],row[2]
    conn.close()
    return rString

from flask import Flask

app = Flask(__name__)



#@app.route('/todo/api/v1.0/tasks', methods=['GET'])
#def get_tasks():
#    return jsonify({'tasks': tasks})


@app.route('/Services/Mobile',methods=['GET'])
def index():
    return "[" + hacequery() + "{}]"

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
