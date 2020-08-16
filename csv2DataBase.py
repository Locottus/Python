import pandas as pd
import glob,os,psycopg2



conn_string = "host='localhost' dbname='clima' user='postgres' password='Guatemala1'"


#global vars
path = "."
all_files = glob.glob(os.path.join(path, "*.txt")) #make list of files in path




def pointConcat(df):
    for index, row in df.iterrows():
        #line =  str(row[0]) + ',' +  str(row[1]) + ',' + str(row[2]) + '.'
        print(row)



def ejecutaComandoPsql(query):
    try:
        print(query)
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
    except:
        write("error en ejecutar comando psql")


def insetQuery(df):
    #print(index,df)
    query0 = "insert into historico_estaciones (estacion,longitud,latitud,zona_vida,year,mes,dia,lluvia,tmax,tmin,etp,bc) values "
    for index, row in df.iterrows():
        #print(row)
        query1 = "('" + str(row[0]) + "'," + str(row[1]) + ","+ str(row[2]) + ",'"+ str(row[3]) + "',"+ str(row[4]) + ","+ str(row[5]) + "," + str(row[6]) + ","  + str(row[7]) + ","+ str(row[8]) + ","+ str(row[9]) + ","+ str(row[10]) + ","+ str(row[11]) + " );"
        ejecutaComandoPsql(query0 + query1)


#main()
print('inicia programa')
for file in all_files:
    # Getting the file name without extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    # Reading the file content to create a DataFrame
    #dataFile = pd.read_csv(file, header=None, sep=',')
    dataFile = pd.read_csv(file, header=0, sep='\t')
    df = pd.DataFrame(dataFile)   
    insetQuery(df)
print('programa terminado')



'''
--proyecto clima
create database clima;

create table historico_estaciones(
	id serial  NOT NULL primary key,
	estacion text not null,
	longitud numeric not null ,
	latitud numeric not null ,
	zona_vida text not null ,
	year numeric not null ,
	mes numeric not null ,
	dia numeric not null ,
	lluvia numeric not null ,
	tmax numeric not null ,
	tmin numeric not null ,
	etp numeric not null ,
	bc numeric not null,
	unique(estacion,longitud,latitud,zona_vida,year,mes,dia,lluvia,tmax,tmin,etp,bc)

);



'''
