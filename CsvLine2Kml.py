import pandas as pd
import glob
import os
import datetime


#global vars
path = "."
all_files = glob.glob(os.path.join(path, "data*.csv")) #make list of files in path
now = datetime.datetime.now() #get current date for output file


f = open('Line' + str(now.day) + str(now.month) + str(now.year)  + '.kml', 'w')#open output file with current date

xmlHeader = '<?xml version="1.0" encoding="UTF-8"?> <kml xmlns="http://earth.google.com/kml/2.0"> <Document> <Placemark>  <LineString>  <coordinates>'
xmlFooter = '</coordinates>  </LineString>  <Style>   <LineStyle> <color>#ff0000ff</color>    <width>5</width>   </LineStyle>  </Style> </Placemark> </Document> </kml>'


def pointConcat(d):
    for index, row in df.iterrows():
        line =  str(row[0]) + ',' +  str(row[1]) + ',' + str(row[2]) + '.'
        f.write(line + '\n')
        print(line)

#main()
f.write(xmlHeader + '\n')#write header

for file in all_files:
    # Getting the file name without extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    # Reading the file content to create a DataFrame
    dataFile = pd.read_csv(file, header=None)
    df = pd.DataFrame(dataFile)   
    pointConcat(df)

f.write(xmlFooter+ '\n')#write footer
f.close()





#my output file contains Longitude,Latitude,Altitude in a csv file.
#-90.5298628393332,14.608550970260422,1524.911447514169,2.1963847,1519558183000,8.0,comment
