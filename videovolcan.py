import os
import psycopg2
from shutil import copyfile
from sys import exit


db_string = 'postgres://postgres:Guatemala1@localhost:5432/hashfiles'
sourceImages = '/home/incyt/servicio/uploads'
destinationVideo = '/home/incyt/servicio/uploads/videos'
temporalFolder ='/videosVolcanes/tmp'
urlVideos = 'https://incyt.url.edu.gt/incyt/api/HashFiles/uploads/videos/'

#disk utils

def dateYesterday():
    from datetime import date
    from datetime import timedelta

    today = date.today() 
    print("Today is: ", today) 
    # Yesterday date 
    yesterday = today - timedelta(days = 1) 
    print("yesterday was: ", yesterday) 
    return yesterday


def copiarImagen(source,target):
    try:
        copyfile(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)



def save():
    os.system("ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y movie.mp4")


def runAllClientsBD():
    y = str(dateYesterday())
    y0 = y + ' 00:00:00'
    y1 = y + ' 23:59:00'
    q = "select filename from filecatalog where fecha between '"+ y0 +"' and '" + y1 + "'  order by fecha asc "
    print(q)
    conn = psycopg2.connect(db_string)
    cursor = conn.cursor()
    cursor.execute(q)
    rows = cursor.fetchall()
 
    for row in rows:
        print(row)
        filename = row[0]
        #copiarImagen('','')

    conn.close()





#void main()
if __name__ == '__main__':
    print("starting")
    runAllClientsBD()
