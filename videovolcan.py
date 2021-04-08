import os
import psycopg2
from sys import exit

#https://www.codegrepper.com/code-examples/python/python+script+to+convert+mp4+to+jpgs

db_string = 'postgres://postgres:Guatemala1@localhost:5432/hashfiles'
sourceImages = '/home/incyt/servicio/uploads'
destinationVideo = '/home/incyt/servicio/uploads/videos'
temporalFolder ='/videosVolcanes/tmp'
pathVideos = '/videosVolcanes/'
urlVideos = 'https://incyt.url.edu.gt/incyt/api/HashFiles/uploads/videos/'

#docker run -it -v /videosVolcanes/tmp:/tmp/ -v /home/incyt/servicio/uploads:/uploads -v /home/incyt/servicio/uploads/videos:/videos -m 2g --cpus=1 --cpu-shares=50 linuxffmpeg
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


#https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python


def saveVideo():
    arch = pathVideos + str(dateYesterday()).replace('-','') + '.mp4'
    imgs = temporalFolder + '/*.jpg' 
    #os.system("ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y archivo.mp4 ")
    #ffmpeg -r 30 -i *.jpg -vcodec mpeg4 -y archivo.mp4
    #ffmpeg -r 200 -i *.jpg -vcodec libx264  -y archivo.mp4
    #os.system("ffmpeg -r 1 -i " + imgs + " -vcodec mpeg4 -y " +  destinationVideo + '/' + arch  )
    print(arch)
    return arch



def vidtest():
#https://pythonexamples.org/python-opencv-cv2-create-video-from-images/#1
    import cv2
    import numpy as np
    import glob

    frameSize = (500, 500)

    out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

    for filename in glob.glob('D:/images/*.jpg'):
        img = cv2.imread(filename)
        out.write(img)

out.release()    

def runYesterdayVideo():
    import moviepy.video.io.ImageSequenceClip
    fps=1

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
        #copiarImagen(sourceImages + '/' + row[0], temporalFolder + '/' + row[0])
        cpCommand = " cp " + sourceImages + '/' + filename + " "  + temporalFolder + '/' + filename
        #print(cpCommand)
        os.system(cpCommand)

    conn.close()
    arch = pathVideos + str(dateYesterday()).replace('-','') + '.mp4'


    image_files = [temporalFolder+'/'+img for img in os.listdir(temporalFolder) if img.endswith(".jpg")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(arch)
    copiarImagen(temporalFolder + '/*.mp4' ,destinationVideo + '/' )

    #query = "insert into videos_volcanes (fecha,video) values (current_timestamp, '" + destinationVideo + '/' + arch + "')"
    #updatetData(query)
    

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



#void main()
if __name__ == '__main__':
    print("starting")
    

    #change to working directory
#    os.chdir(pathVideos)

    path = os.getcwd()
    print ("The current working directory is %s" % path)

    try:
        os.system( ' rm -rf ' + pathVideos )
        #shutil.rmtree(temporalFolder, ignore_errors=True)
    except:
        print('cannot delete folder',pathVideos)

        
    try:
        os.system( ' rm -rf ' + temporalFolder )
        #shutil.rmtree(temporalFolder, ignore_errors=True)
    except:
        print('cannot delete folder',temporalFolder)

    try:
        os.mkdir(temporalFolder)
    except OSError:
        print ("Creation of the directory %s failed" % path)

    vidtest()    
    #runYesterdayVideo()
