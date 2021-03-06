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

fname = 'Polygon' + str(now.day) + str(now.month) + str(now.year)  + '.kml'
f = open(fname , 'w')#open output file with current date

xmlHeader = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>\n"""

xmlFooter = '\n</Document>\n</kml>\n'


def pointConcat(df):
    for index, row in df.iterrows():
        line =  str(row[0]) + ',' +  str(row[1]) + ',' + str(row[2]) + '.'
        f.write(line + '\n')
        print(line)

def polygonCreation(df,p):
    line = """\n<Placemark>
		<name>""" + p + """</name>
		<Polygon>
			<tessellate>1</tessellate>
			<extrude>1</extrude>
			<gx:altitudeMode>relativeToGround</gx:altitudeMode>
			<outerBoundaryIs>
				<LinearRing>
					<coordinates>\n"""
    f.write(line)
    strude = str(decimal.Decimal(random.randrange(250, 400))/100)#random strude from 2.50 to 4.00
    for index, row in df.iterrows():
        if ((str(row[6]) == p )):
            line = str(row[0]) + ',' +  str(row[1]) + ',' + strude
            f.write(line + '\n')
            print(line)
    line = """					</coordinates>
				</LinearRing>
			</outerBoundaryIs>
		</Polygon>
	</Placemark>
\n"""
    f.write(line)

def isPolygon(df,p):
    for index, row in df.iterrows():
        if ((str(row[6]) == str(p))):
            return row[7];
    return False
    
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
        if (isPolygon(df,p)):
            print('******' + str(p))
            polygonCreation(df,str(p))
        
    #pointConcat(df)

f.write(xmlFooter+ '\n')#write footer
f.close()
print('end of line')





#my output file contains Longitude,Latitude,Altitude in a csv file.
#-90.5298628393332,14.608550970260422,1524.911447514169,2.1963847,1519558183000,8.0,comment,TRUE,num_poly
