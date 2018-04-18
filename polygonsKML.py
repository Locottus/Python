import pandas as pd
import glob
import os
import datetime

import random
import decimal

#https://developers.google.com/kml/documentation/kml_tut
#global vars
path = "."
all_files = glob.glob(os.path.join(path, "*.csv")) #make list of files in path
now = datetime.datetime.now() #get current date for output file


f = open('Line' + str(now.day) + str(now.month) + str(now.year)  + '.kml', 'w')#open output file with current date

xmlHeader = '<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Placemark>\n<name>MGM Poligonos</name>\n<Polygon>\n<extrude>1</extrude>\n<altitudeMode>relativeToGround</altitudeMode>\n'
xmlFooter = '\n</Polygon>\n</Placemark>\n</kml>\n'


def pointConcat(df):
    for index, row in df.iterrows():
        line =  str(row[0]) + ',' +  str(row[1]) + ',' + str(row[2]) + '.'
        f.write(line + '\n')
        print(line)

def polygonCreation(df,p):
    line = '\n<outerBoundaryIs>\n<LinearRing>\n<coordinates>\n'
    f.write(line)
    strude = str(decimal.Decimal(random.randrange(250, 400))/100)#random strude from 2.50 to 4.00
    for index, row in df.iterrows():
        if (str(row[6]) == p ):
            line = str(row[0]) + ',' +  str(row[1]) + ',' + strude
            f.write(line + '\n')
            print(line)
    line = '\n</coordinates>\n</LinearRing>\n</outerBoundaryIs>\n'
    f.write(line)
    
#main()
f.write(xmlHeader + '\n')#write header

for file in all_files:
    # Getting the file name without extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    # Reading the file content to create a DataFrame
    dataFile = pd.read_csv(file, header=None)
    df = pd.DataFrame(dataFile)
    polygons = df[6].unique()
    for p in polygons:
        print('******' + p)
        polygonCreation(df,p)
        
    #pointConcat(df)

f.write(xmlFooter+ '\n')#write footer
f.close()





#my output file contains Longitude,Latitude,Altitude in a csv file.
#-90.5298628393332,14.608550970260422,1524.911447514169,2.1963847,1519558183000,8.0,comment
