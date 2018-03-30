import pandas as pd
import pyproj
import glob
import os
import datetime

#first install the following c++ for python library
#https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266

#run python setup.py install
#https://jswhit.github.io/pyproj/

#program is now ready to be used.

#docu
#https://pypi.python.org/pypi/pyproj?


#global vars
path = "."
all_files = glob.glob(os.path.join(path, "*.csv")) #make list of files in path
now = datetime.datetime.now() #get current date for output file
f = open('PuntoUTM' + str(now.day) + str(now.month) + str(now.year)  + '.txt', 'w')#open output file with current date

def Point2UTM(x,y):
# projection 1: UTM zone 15, grs80 ellipse, NAD83 datum
# (defined by epsg code 26915)
    p1 = pyproj.Proj(init='epsg:26915')
    return p1(x,y)


def pointConcat(df):
    line = ''
    print (df)
    for index, row in df.iterrows():
        if (str(row[0]) <> '0.0'):
            x1, y1 = Point2UTM(row[0],row[1])            
            line =  str(x1) + ',' + str(y1) + ',' + str(row[2]) + ',' + str(row[3]) + ','+ str(row[4]) + ',' + str(row[5]) + ',' + str(row[6])
            print(line)
            f.write(line + '\n')
    


#void main()
print('starting compilation')
for file in all_files:
    # Getting the file name without extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    # Reading the file content to create a DataFrame
    dataFile = pd.read_csv(file, header=None)
    df = pd.DataFrame(dataFile)   
    pointConcat(df)   
print('end of line.')
f.close()





#my input file contains Longitude,Latitude,Altitude in a csv file.
#-90.5298628393332,14.608550970260422,1524.911447514169,2.1963847,1519558183000,8.0,comment
