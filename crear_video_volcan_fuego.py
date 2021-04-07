import os
import psycopg2
from sys import exit
import cv2
import numpy as np

db_string = 'postgres://postgres:postgres2020!Incyt@172.17.250.12:5432/hashFiles'
#db_string = 'postgres://postgres:Guatemala1@localhost:5432/hashfiles'
sourceImages = '/home/incyt/servicio/uploads'
destinationVideo = '/home/incyt/servicio/uploads/videos_volcanes'
#temporalFolder ='/videosVolcanes/tmp'
#pathVideos = '/videosVolcanes/'
urlVideos = 'https://incyt.url.edu.gt/incyt/api/HashFiles/uploads/videos_volcanes/'

#docker run -it -v /videosVolcanes/tmp:/tmp/ -v /home/incyt/servicio/uploads:/uploads -v /home/incyt/servicio/uploads/videos:/videos -m 2g --cpus=1 --cpu-shares=50 linuxffmpeg
#disk utils

files = []
fps = 30
frame_array = []

def dateYesterday():
    from datetime import date
    from datetime import timedelta

    today = date.today() 
    print("Today is: ", today) 
    # Yesterday date 
    yesterday = today - timedelta(days = 1) 
    print("yesterday was: ", yesterday) 
    return yesterday


def runYesterdayVideo():

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
        filename = row[0] + '.jpg'
        files.append(sourceImages + '/' + filename)
    conn.close()
    print("number of images to process:" , len(files))
    #print(files)
    archName = str(dateYesterday()).replace('-','') + '.avi'
    arch = destinationVideo + '/' + archName
    print(arch)
    for i in range(len(files)):
        img = cv2.imread(files[i])
        size = (640,480)
        frame_array.append(img)
    out = cv2.VideoWriter(arch,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    
    query = "insert into videos_volcanes (fecha,video) values (current_timestamp, '" +  urlVideos + archName + "')"
    updatetData(query)

    print('end')

   

def updatetData(query):
    print(query)
    conn = psycopg2.connect(db_string)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except:
        print('*************************** could not insert*********************************')
        print(query)
    conn.commit()
    conn.close()


#https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481

#void main()
if __name__ == '__main__':
    print("starting")
    runYesterdayVideo()

