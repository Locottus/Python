import pandas as pd
import glob,os,psycopg2



conn_string = "host='localhost' dbname='clima' user='postgres' password='Guatemala1'"
#conn_string = "host='localhost' dbname='hambre' user='postgres' password='Guatemala1'"


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
        write("error en ejecutar comando psql",query)


def insetQueryClima(df):
    #print(index,df)
    query0 = "insert into historico_estaciones (estacion,longitud,latitud,zona_vida,year,mes,dia,lluvia,tmax,tmin,etp,bc) values "
    for index, row in df.iterrows():
        #print(row)
        query1 = "('" + str(row[0]) + "','" + str(row[1]) + "','"+ str(row[2]) + "','"+ str(row[3]) + "','"+ str(row[4]) + "','"+ str(row[5]) + "','" + str(row[6]) + "','"  + str(row[7]) + "','"+ str(row[8]) + "','"+ str(row[9]) + "','"+ str(row[10]) + "','"+ str(row[11]) + "' );"
        ejecutaComandoPsql(query0 + query1)



def proyectoClima():
    print('inicia proyecto clima')
    for file in all_files:
        # Getting the file name without extension
        file_name = os.path.splitext(os.path.basename(file))[0]
        print(file_name)
        # Reading the file content to create a DataFrame
        #dataFile = pd.read_csv(file, header=None, sep=',')
        dataFile = pd.read_csv(file, header=0, sep='\t', encoding = "ISO-8859-1", error_bad_lines=False, index_col=False, dtype='unicode')
        df = pd.DataFrame(dataFile)   
        insetQueryClima(df)






def insetQueryHambre(df):
    #print(index,df)

                
    query0 = "insert into historico (FECHA_NOTIFICACION	,NO_FICHA   ,SEMANA	,NOTIFICACION_AREA	,NOTIFICACION_DEPARTAMENTO	,NOTIFICACION_MUNICIPIO	,NOTIFICACION_DISTRITO	,CENTRO_SALUD	,PUESTO_SALUD	,CENTRO_CONVERGENCIA	,NOTIFICACION_TIPO_SERVICIO	,NOTIFICACION_SERVICIO	,NOTIFICACION_OTRO_SERVICIO	,ESTABLECIMIENTO_PRIVADO	,HOSPITAL	,ESTABLECIMIENTO	,CODIGO_NOMBRE	,FECHA_NACIMIENTO	,EDAD_ANIOS	,EDAD_MESES	,PROCEDENCIA_DEPARTAMENTO	,PROCEDENCIA_MUNICIPIO	,PROCEDENCIA_LOCALIDAD	,PROCEDENCIA_LOCALIDAD_OTRA	,GRUPO_ETNICO	,OTRA_ETNIA	,SEXO	,PESO	,TALLA	,PARENTESCO	,FECHA_DETECCION	,LACTANCIA_MENOR_SEIS	,LACTANCIA_SEIS_DOS	,ACTUAL_TOS	,ACTUAL_FIEBRE	,ACTUAL_DIARREA	,ACTUAL_EDEMA	,ANTES_TOS	,ANTES_FIEBRE	,ANTES_DIARREA	,ANTES_EDEMA	,EDEMA_ANTERIOR	,TRATAMIENTO	,TRATAMIENTO_TIEMPO	,PESO_NACER	,HEMANOS_MENORES	,HERMANOS_MAYORES	,MENORES_FALLECIDOS	,MENORES_EDEMA	,ABASTECIMIENTO_AGUA	,OTRO_ABASTECIMIENTO_AGUA	,DISPOSICION_EXCRETAS	,DISPOSICION_EXCRETAS_OTRO	,DISPOSICION_BASURA	,DISPOSICION_BASURA_OTRO	,SITUACION_LABORAL	,INGRESO_FAMILIAR	,TIPO_VIVIENDA	,FUENTE_INGRESO1	,FUENTE_INGRESO2	,FUENTE_INGRESO3	,RECIBE_AYUDA_EXTRANJERO	,MFAMILIA_PROGRESA	,BOLSA_SOLIDARIA	,MCOMUNI_PRODUCE	,MAGA_BOLSA	,MAGA_PROYECTOS	,MAGA_FERTILIZANTES	,MAGA_HUERTOS	,MAGA_POLLOS	,MAGA_GALLINAS	,PRORURAL	,AGUAFUENTEPAZ	,OTROS_FACTOR_RIESGO	,HA_VENDIDO	,RESERVA_ALIMENTOS	,TIEMPO_RESERVA	,TIEMPOS_COMIDA	,DIAGNOSTICO_CLINICO,DIAGNOSTICO_MEDICION,REFERIDO   ,REFERIDO_DONDE	,CONDICION  ) values "
    for index, row in df.iterrows():

        try:
            query1 = "('" + str(row[0]).replace("'"," ")+ "','" + str(row[1]).replace("'"," ")+ "','"+ str(row[2]).replace("'"," ")+ "','"+ str(row[3]).replace("'"," ")+ "','"+ str(row[4]).replace("'"," ")+ "','"+ str(row[5]).replace("'"," ")+ "','" + str(row[6]).replace("'"," ")+ "','"  + str(row[7]).replace("'"," ")+ "','"+ str(row[8]).replace("'"," ")+ "','"+ str(row[9]).replace("'"," ")+ "','"+ str(row[10]).replace("'"," ") + "','" #+ str(row[11]).replace("'"," ")+ " );"
            query2 =   str(row[11]).replace("'"," ")+ "','" + str(row[12]).replace("'"," ")+ "','"+ str(row[13]).replace("'"," ")+ "','"+ str(row[14]).replace("'"," ")+ "','"+ str(row[15]).replace("'"," ")+ "','"+ str(row[16]).replace("'"," ")+ "','" + str(row[17]).replace("'"," ")+ "','"  + str(row[18]).replace("'"," ")+ "','"+ str(row[19]).replace("'"," ")+ "','"+ str(row[20]).replace("'"," ")+ "','"
            query3 =   str(row[21]).replace("'"," ")+ "','" + str(row[22]).replace("'"," ")+ "','"+ str(row[23]).replace("'"," ")+ "','"+ str(row[24]).replace("'"," ")+ "','"+ str(row[25]).replace("'"," ")+ "','"+ str(row[26]).replace("'"," ")+ "','" + str(row[27]).replace("'"," ")+ "','"  + str(row[28]).replace("'"," ")+ "','"+ str(row[29]).replace("'"," ")+ "','"+ str(row[30]).replace("'"," ")+ "','"
            query4 =   str(row[31]).replace("'"," ")+ "','" + str(row[32]).replace("'"," ")+ "','"+ str(row[33]).replace("'"," ")+ "','"+ str(row[34]).replace("'"," ")+ "','"+ str(row[35]).replace("'"," ")+ "','"+ str(row[36]).replace("'"," ")+ "','" + str(row[37]).replace("'"," ")+ "','"  + str(row[38]).replace("'"," ")+ "','"+ str(row[39]).replace("'"," ")+ "','"+ str(row[40]).replace("'"," ")+ "','"
            query5 =   str(row[41]).replace("'"," ")+ "','" + str(row[42]).replace("'"," ")+ "','"+ str(row[43]).replace("'"," ")+ "','"+ str(row[44]).replace("'"," ")+ "','"+ str(row[45]).replace("'"," ")+ "','"+ str(row[46]).replace("'"," ")+ "','" + str(row[47]).replace("'"," ")+ "','"  + str(row[48]).replace("'"," ")+ "','"+ str(row[49]).replace("'"," ")+ "','"+ str(row[50]).replace("'"," ")+ "','"

            query6 =   str(row[51]).replace("'"," ")+ "','" + str(row[52]).replace("'"," ")+ "','"+ str(row[53]).replace("'"," ")+ "','"+ str(row[54]).replace("'"," ")+ "','"+ str(row[55]).replace("'"," ")+ "','"+ str(row[56]).replace("'"," ")+ "','" + str(row[57]).replace("'"," ")+ "','"  + str(row[58]).replace("'"," ")+ "','"+ str(row[59]).replace("'"," ")+ "','"+ str(row[60]).replace("'"," ")+ "','"
            query7 =   str(row[61]).replace("'"," ")+ "','" + str(row[62]).replace("'"," ")+ "','"+ str(row[63]).replace("'"," ")+ "','"+ str(row[64]).replace("'"," ")+ "','"+ str(row[65]).replace("'"," ")+ "','"+ str(row[66]).replace("'"," ")+ "','" + str(row[67]).replace("'"," ")+ "','"  + str(row[68]).replace("'"," ")+ "','"+ str(row[69]).replace("'"," ")+ "','"+ str(row[70]).replace("'"," ")+ "','"
            query8 =   str(row[71]).replace("'"," ")+ "','" + str(row[72]).replace("'"," ")+ "','"+ str(row[73]).replace("'"," ")+ "','"+ str(row[74]).replace("'"," ")+ "','"+ str(row[75]).replace("'"," ")+ "','"+ str(row[76]).replace("'"," ")+ "','" + str(row[77]).replace("'"," ")+ "','"  + str(row[78]).replace("'"," ")+ "','"+ str(row[79]).replace("'"," ")+ "','"+ str(row[80]).replace("'"," ")+ "','"
            query9 =   str(row[81]).replace("'"," ")+ "','" + str(row[82]).replace("'"," ")+ "');"

            #print(query0,query1,query2,query3,query4,query5,query6,query7,query8,query9)
            #print('')
            ejecutaComandoPsql(query0+query1+query2+query3+query4+query5+query6+query7+query8+query9)

        except:
            print('error en creacion de query, pero continuamos')

def proyectoHambre():
    print('inicia proyecto hambre')
    for file in all_files:
        print('*****************************************************************************')
        print(file)
        file_name = os.path.splitext(os.path.basename(file))[0]
        dataFile = pd.read_csv(file, header=0, sep='\t', encoding = "ISO-8859-1", error_bad_lines=False, index_col=False, dtype='unicode')
        df = pd.DataFrame(dataFile)
        print(df.replace(to_replace = "'", value = " "))
        insetQueryHambre(df)


#main()
print('inicia programa')
proyectoClima()
#proyectoHambre()
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






--proyecto hambre

create database hambre;

create table historico (	
    id serial  NOT NULL primary key,
    FECHA_NOTIFICACION	  text not null,
    NO_FICHA	  text not null,
    SEMANA	  text not null,
    NOTIFICACION_AREA	  text not null,
    NOTIFICACION_DEPARTAMENTO	  text not null,
    NOTIFICACION_MUNICIPIO	  text not null,
    NOTIFICACION_DISTRITO	  text not null,
    CENTRO_SALUD	  text not null,
    PUESTO_SALUD	  text not null,
    CENTRO_CONVERGENCIA	  text not null,
    NOTIFICACION_TIPO_SERVICIO	  text not null,
    NOTIFICACION_SERVICIO	  text not null,
    NOTIFICACION_OTRO_SERVICIO	  text not null,
    ESTABLECIMIENTO_PRIVADO	  text not null,
    HOSPITAL	  text not null,
    ESTABLECIMIENTO	  text not null,
    CODIGO_NOMBRE	  text not null,
    FECHA_NACIMIENTO	  text not null,
    EDAD_ANIOS	  text not null,
    EDAD_MESES	  text not null,
    PROCEDENCIA_DEPARTAMENTO	  text not null,
    PROCEDENCIA_MUNICIPIO	  text not null,
    PROCEDENCIA_LOCALIDAD	  text not null,
    PROCEDENCIA_LOCALIDAD_OTRA	  text not null,
    GRUPO_ETNICO	  text not null,
    OTRA_ETNIA	  text not null,
    SEXO	  text not null,
    PESO	  text not null,
    TALLA	  text not null,
    PARENTESCO	  text not null,
    FECHA_DETECCION	  text not null,
    LACTANCIA_MENOR_SEIS	  text not null,
    LACTANCIA_SEIS_DOS	  text not null,
    ACTUAL_TOS	  text not null,
    ACTUAL_FIEBRE	  text not null,
    ACTUAL_DIARREA	  text not null,
    ACTUAL_EDEMA	  text not null,
    ANTES_TOS	  text not null,
    ANTES_FIEBRE	  text not null,
    ANTES_DIARREA	  text not null,
    ANTES_EDEMA	  text not null,
    EDEMA_ANTERIOR	  text not null,
    TRATAMIENTO	  text not null,
    TRATAMIENTO_TIEMPO	  text not null,
    PESO_NACER	  text not null,
    HEMANOS_MENORES	  text not null,
    HERMANOS_MAYORES	  text not null,
    MENORES_FALLECIDOS	  text not null,
    MENORES_EDEMA	  text not null,
    ABASTECIMIENTO_AGUA	  text not null,
    OTRO_ABASTECIMIENTO_AGUA	  text not null,
    DISPOSICION_EXCRETAS	  text not null,
    DISPOSICION_EXCRETAS_OTRO	  text not null,
    DISPOSICION_BASURA	  text not null,
    DISPOSICION_BASURA_OTRO	  text not null,
    SITUACION_LABORAL	  text not null,
    INGRESO_FAMILIAR	  text not null,
    TIPO_VIVIENDA	  text not null,
    FUENTE_INGRESO1	  text not null,
    FUENTE_INGRESO2	  text not null,
    FUENTE_INGRESO3	  text not null,
    RECIBE_AYUDA_EXTRANJERO	  text not null,
    MFAMILIA_PROGRESA	  text not null,
    BOLSA_SOLIDARIA	  text not null,
    MCOMUNI_PRODUCE	  text not null,
    MAGA_BOLSA	  text not null,
    MAGA_PROYECTOS	  text not null,
    MAGA_FERTILIZANTES	  text not null,
    MAGA_HUERTOS	  text not null,
    MAGA_POLLOS	  text not null,
    MAGA_GALLINAS	  text not null,
    PRORURAL	  text not null,
    AGUAFUENTEPAZ	  text not null,
    OTROS_FACTOR_RIESGO	  text not null,
    HA_VENDIDO	  text not null,
    RESERVA_ALIMENTOS	  text not null,
    TIEMPO_RESERVA	  text not null,
    TIEMPOS_COMIDA	  text not null,
    DIAGNOSTICO_CLINICO	  text not null,
    DIAGNOSTICO_MEDICION	  text not null,
    REFERIDO	  text not null,
    REFERIDO_DONDE	  text not null,
    CONDICION	  text not null

)	



'''
