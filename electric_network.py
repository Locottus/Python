################################################################################################################################################
################################################################################################################################################
import cx_Oracle,os,sys,time,csv,arcpy

#F_POSTE = r'C:\GIS\TMP.gdb\POSTES'
F_POSTE = r'Database Connections\SDE@SERVGISBD.sde\sde.DBO.POSTES_EEGSA'

Feat = r'C:\GIS\TMP.gdb\TBL_XYLINE'
ListaPostes = []

FNuds = r'C:\compartida\GN.gdb\NUDS'
NUDS = []

PRIMARIO_DGNS = r'C:\GIS\TMP.gdb\LINEPRIM2010'
SECUNDARIO_DGNS = r'C:\GIS\TMP.gdb\LINESEC2010'

PRIMARIO_MSLINK = r'C:\GIS\TMP.gdb\Primario_tbl' 
SECUNDARIO_MSLINK = r'C:\GIS\TMP.gdb\Secundario_tbl'


def busca_Poste(POSTE):
    for x in ListaPostes :
        if int(x[0]) == int(POSTE):
            #print " gefundet P" , x
            return x
    return [0,0]

def busca_Poste2(OBJECTID):
    for x in ListaPostes :
        if int(x[3]) == int(OBJECTID):
            #print " gefundet P" , x
            return x
    return [0,0]

def Carga_postes():
    print "cargando postes (poste, x, y)"
    rows = arcpy.SearchCursor(F_POSTE,"","","POSTE;X;Y;OBJECTID")
    for rowS in rows:
        ListaPostes.append([int(rowS.POSTE),rowS.X,rowS.Y,rowS.OBJECTID])
    print " postes cargados: ",len(ListaPostes)



def Linea_x1_x2(mslink,tipo_linea):
    Postes = []
    P = []
    ip = '172.16.2.26' 
    port = 1521 
    SID = 'GIS'
    query = 'select pc.poste, p.identificador from poste_conductor pc, poste p where conductor = '+ str(mslink)+ ' and pc.poste = p.mslink order by poste asc'
    try:
        dsn_tns = cx_Oracle.makedsn(ip, port, SID) 
        connection = cx_Oracle.connect('herlich', 'herlich', dsn_tns)
        cursor = connection.cursor()
        cursor.execute(query)
        lRows = cursor.fetchall()
        for lRow in lRows:
            try:
                if int(lRow[0] > 0):#[0,0]
                    tmp = busca_Poste(int(lRow[1]))
                    try:
                        if (tmp[0] > 0 ) :
                            P.append(tmp)
                    except:
                        pass
            except Exception, e:
                pass
               #print  e.message,P,tmp
        cursor.close()
        connection.close()
        #print 'tamanio lista:',len(P)
        s = ''
        a = 0
        
#        if len(P) == 1:#esto es para crear otro punto para hacer la linea
#            s = str(mslink) + ','+ str(P[a][1]) + ',' + str(P[a][2]) + ',' + str(P[a][1]) +','+ str(P[a][2])+',' + str(tipo_linea) + ',' + str(P[a][0]) + ',' + str(P[a][0]) +'\n'
#            Arch.write(s)
            #print '*',s#mslink,P[a][1],P[a][2], P[a][1],P[a][2],tipo_linea,str(P[a][0]),str(P[a][0])
            #Arch.write("OK1 " + str(P) + '\n' )
        if len(P) > 1:
            while a < len(P) - 1:
                s = str(mslink)+','+str(P[a][1]) + ','+ str(P[a][2]) + ',' + str(P[a + 1][1]) + ',' + str(P[a + 1][2])+  ',' + str(tipo_linea) + ',' +  str(P[a][0]) + ',' + str(P[a+1][0]) +'\n'
                Arch.write(s)
                a = a + 1
    except Exception, e:
        print  e.message,P



def Linea_mslink(query,tipo_linea):
    ip = '172.16.2.26' 
    port = 1521 
    SID = 'GIS'
#    query = 'select distinct mslink from conductor_primario order by mslink' 
    try:
        dsn_tns = cx_Oracle.makedsn(ip, port, SID) 
        connection = cx_Oracle.connect('herlich', 'herlich', dsn_tns)
        cursor = connection.cursor()
        cursor.execute(query)
        lRows = cursor.fetchall()
        for lRow in lRows:
            #print "MSLINK:" ,lRow[0]
            Linea_x1_x2(int(lRow[0]),tipo_linea)
        cursor.close()
        connection.close()
    except Exception, e:
        print  e.message



def inserta_tabla(Archivo):
    arcpy.DeleteRows_management(Feat)
    from arcpy import gp
    print'insertando a la tabla xylinea'
    reader = csv.reader(open( Archivo , "rb"),delimiter = ',')
    #update capa f_poste
    contador = 1
    for listrow in reader:
        if contador > 0:
            print listrow, str(contador)
            try:
                gp.Workspace = Feat
                cur =gp.InsertCursor(Feat)
                row = cur.NewRow()
                row.MSLINK = listrow[0]
                row.X1 = listrow[1]
                row.Y1 = listrow[2]
                row.X2 = listrow[3]
                row.Y2 = listrow[4]
                row.TIPO_LINEA = listrow[5]
                row.POSTE1 = listrow[6]
                row.POSTE2 = listrow[7]                
                cur.InsertRow(row)
                del row
            except Exception, e:
                print  e.message
        contador = contador + 1


    


def leer_directorio():
    print " comienza la busqueda de todos los nuds" 
    directorio = r'Z:\DGNS'    
    contador = 0
    Arch = open("NUDS.csv","w")#abre archivo tmp a trabajar
    Arch.write("contador,letra,x,y \n")
    for x in os.listdir(directorio):
        x = x.upper()        
        if x.find("GDB",0) > 0:

            s = directorio + r'\\'+x+r'\\Q35'
            print "directory: ",s,len(x)
            try:
                    rows = arcpy.SearchCursor(s,"","","TextString;igds_insertion_x; igds_insertion_y")
                    for rowS in rows:
                        contador = contador + 1                        
                        print contador,rowS.TextString,rowS.igds_insertion_x, rowS.igds_insertion_y
                        Arch.write(str(contador) + ","+ str(rowS.TextString) + "," + str(rowS.igds_insertion_x) + "," + str(rowS.igds_insertion_y) + "\n")

                    del rowS, rows
            except Exception, e:
                print e.message
                print arcpy.GetMessages()
    Arch.close()




def analiza_Nuds():
    print "creando near de nuds con nuds"
    arcpy.Near_analysis( FNuds,FNuds, "3 Meters", "LOCATION", "NO_ANGLE")
    try:
        print"agregando campo tipo_linea"
        arcpy.AddField_management(FNuds, "TIPO_LINEA", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")
    except Exception, e:
        print "Ya existe el campo"

    print"actualizando tipos de linea"
    rows = arcpy.SearchCursor(FNuds,"","","OBJECTID;NEAR_DIST;NEAR_X;NEAR_Y;NEAR_FID")
    for row in rows:
        NUDS.append([row.OBJECTID,row.NEAR_DIST,row.NEAR_X,row.NEAR_Y,row.NEAR_FID])
#actualizo los nuds de todas las lineas
    for x in NUDS:
        print "analizando:",x
        cur = arcpy.UpdateCursor(FNuds, " OBJECTID = " + str(x[0]))
        for rowU in cur:
            if float(x[1]) == -1:
                rowU.TIPO_LINEA = 0
            else:
                if float(x[0]) < float(x[4]):
                    rowU.TIPO_LINEA = 2
                else:
                    rowU.TIPO_LINEA = 1
            cur.updateRow(rowU)
        del cur, rowU

    print"creo features para NUD primario y NUD secundario"
    try:
        arcpy.DeleteFeatures_management(FNuds+"_Primario")
    except Exception, e:
        print "No hay capa de fnuds_primario"

    try:
        arcpy.DeleteFeatures_management(FNuds+"_Secundario")        
    except Exception, e:
        print "No hay capa de fnuds_secundario"

    try:
        print" Process: Select primario"
        arcpy.Select_analysis(FNuds,FNuds+"_Primario" , "\"TIPO_LINEA\" in (0,1)")
    except Exception, e:
        print "No se pudo crear la capa de fnuds primarios"

    try:
        print" Process: Select secundario"
        arcpy.Select_analysis(FNuds,FNuds+"_Secundario" , "\"TIPO_LINEA\" in (0,2)")
    except Exception, e:
        print "No se pudo crear la capa de fnuds secundarios"





        
def analiza_Postes_lineas():
# Local variables:

    print 'nuds primario dgn'
    NUDS_Primario = "C:\compartida\ACTIVOS.gdb\NUDS_Primario"
    Primario_DGN = "C:\compartida\ACTIVOS.gdb\LINEPRIM2010"
    tbl_nuds_primario = "C:\\compartida\\ACTIVOS.gdb\\tbl_nuds_primario"
    arcpy.GenerateNearTable_analysis(NUDS_Primario, Primario_DGN, tbl_nuds_primario, "5 Meters", "NO_LOCATION", "NO_ANGLE", "ALL", "4")

    print 'primario postes'
    NUDS_Primario = "C:\compartida\ACTIVOS.gdb\POSTES_EEGSA_Project"
    Primario_DGN = "C:\compartida\ACTIVOS.gdb\LINEPRIM2010"
    tbl_nuds_primario = "C:\\compartida\\ACTIVOS.gdb\\tbl_poste_primario"
    arcpy.GenerateNearTable_analysis(NUDS_Primario, Primario_DGN, tbl_nuds_primario, "5 Meters", "NO_LOCATION", "NO_ANGLE", "ALL", "4")

    print 'nuds secundario dgn'
    NUDS_Primario = "C:\compartida\ACTIVOS.gdb\NUDS_Secundario"
    Primario_DGN = "C:\compartida\ACTIVOS.gdb\LINESEC2010"
    tbl_nuds_primario = "C:\\compartida\\ACTIVOS.gdb\\tbl_nuds_secundario"
    arcpy.GenerateNearTable_analysis(NUDS_Primario, Primario_DGN, tbl_nuds_primario, "5 Meters", "NO_LOCATION", "NO_ANGLE", "ALL", "4")

    print'postes con linea secundaria'
    NUDS_Primario = "C:\compartida\ACTIVOS.gdb\POSTES_EEGSA_Project"
    Primario_DGN = "C:\compartida\ACTIVOS.gdb\LINESEC2010"
    tbl_nuds_primario = "C:\\compartida\\ACTIVOS.gdb\\tbl_poste_secundario"
    arcpy.GenerateNearTable_analysis(NUDS_Primario, Primario_DGN, tbl_nuds_primario, "5 Meters", "NO_LOCATION", "NO_ANGLE", "ALL", "4")





def tabla_poste_conductor(feature,objecto,x1,y1):
    r1 = arcpy.SearchCursor(feature,"NEAR_FID = " + str(objecto),"","IN_FID;NEAR_FID;NEAR_DIST")
    from arcpy import gp    
    for r11 in r1:
        x = busca_Poste2(r11.IN_FID)
        APN.write( str(x[1])+","+str(x[2])+","+str(x1)+","+str(y1)+","+str(x[0])+"\n" )
        print "(", x[1],",",x[2],")", "(", x1,",",y1,")",x[0]
        


def tabla_nud_conductor2(feature,objecto,x1,y1):
    r1 = arcpy.SearchCursor(feature,"IN_FID = " + str(objecto),"","IN_FID;NEAR_FID;NEAR_DIST")
    for r11 in r1:
        tabla_poste_conductor(r"C:\compartida\ACTIVOS.gdb\tbl_poste_secundario",r11.NEAR_FID,x1,y1)



def tabla_nud_conductor(feature,objecto,x1,y1):
    r1 = arcpy.SearchCursor(feature,"IN_FID = " + str(objecto),"","IN_FID;NEAR_FID;NEAR_DIST")
    for r11 in r1:
        tabla_poste_conductor(r"C:\compartida\ACTIVOS.gdb\tbl_poste_primario",r11.NEAR_FID,x1,y1)

    

def recorre_tabla_nuds_primario():
    print 'inicia el recorrido de la tabla de nuds con primarios'
    rows = arcpy.SearchCursor(r'C:\compartida\ACTIVOS.gdb\NUDS_Primario',"","","OBJECTID;X;Y")
    for row in rows:
        tabla_nud_conductor(r'C:\compartida\ACTIVOS.gdb\tbl_nuds_primario',row.OBJECTID,row.X, row.Y)
    


def recorre_tabla_nuds_secundario():
    print 'inicia el recorrido de la tabla de nuds con primarios'
    rows = arcpy.SearchCursor(r'C:\compartida\ACTIVOS.gdb\NUDS_Secundario',"","","OBJECTID;X;Y")
    for row in rows:
        tabla_nud_conductor2(r'C:\compartida\ACTIVOS.gdb\tbl_nuds_secundario',row.OBJECTID,row.X, row.Y)
    


def inserta_tabla2(archivo,Feat):

    arcpy.DeleteRows_management(Feat)
    from arcpy import gp
    print'insertando a la tabla xylinea'
    reader = csv.reader(open( archivo , "rb"),delimiter = ',')
    #update capa f_poste
    contador = 0
    for listrow in reader:
        if contador > 0:
            print listrow, str(contador),Feat
            try:
                gp.Workspace = Feat
                cur =gp.InsertCursor(Feat)
                row = cur.NewRow()
                row.X1 = listrow[0]
                row.Y1 = listrow[1]
                row.X2 = listrow[2]
                row.Y2 = listrow[3]
                row.POSTE = listrow[4]
                cur.InsertRow(row)
                del row
            except Exception, e:
                print  e.message
        contador = contador + 1



def crea_puntos_lineas():
    try:
        # Local variables:
        TBL_XYLINE = "C:\\GIS\\TMP2.gdb\\TBL_XYLINE"
        TBL_XYLINE_TableSelect = "C:\\GIS\\TMP2.gdb\\TBL_XYLINE_P"
        feature = r'C:\GIS\TMP2.gdb\PRIMARIO_Projected'
        # Process: Table Select
        print "procesando primarios"
        try:
            arcpy.Delete_management(TBL_XYLINE_TableSelect, "Table")
        except:
            pass
        try:
            arcpy.TableSelect_analysis(TBL_XYLINE, TBL_XYLINE_TableSelect, "\"TIPO_LINEA\" = '1'")
        except:
            pass
        try:
            arcpy.Delete_management(feature, "FeatureClass")
        except:
            pass
    except Exception, e:
        print  e.message
        print arcpy.GetMessages()


    try:
        # Local variables:
        TBL_XYLINE = "C:\\GIS\\TMP2.gdb\\TBL_XYLINE"
        TBL_XYLINE_TableSelect = "C:\\GIS\\TMP2.gdb\\TBL_XYLINE_S"
        feature = r'C:\GIS\TMP2.gdb\SECUNDARIO_Projected'
        # Process: Table Select
        print "procesando primarios"
        try:
            arcpy.Delete_management(TBL_XYLINE_TableSelect, "Table")
        except:
            pass
        try:
            arcpy.TableSelect_analysis(TBL_XYLINE, TBL_XYLINE_TableSelect, "\"TIPO_LINEA\" = '2'")
        except:
            pass
        try:
            arcpy.Delete_management(feature, "FeatureClass")
        except:
            pass
    except Exception, e:
        print  e.message
        print arcpy.GetMessages()




    try:
        # Local variables:
        TBL_XYLINE = "C:\\GIS\\TMP2.gdb\\TBL_XYLINE"
        TBL_XYLINE_TableSelect = "C:\\GIS\\TMP2.gdb\\TBL_XYLINE_A"
        feature = r'C:\GIS\TMP2.gdb\AT_Projected'
        # Process: Table Select
        print "procesando primarios"
        try:
            arcpy.Delete_management(TBL_XYLINE_TableSelect, "Table")
        except:
            pass
        try:
            arcpy.TableSelect_analysis(TBL_XYLINE, TBL_XYLINE_TableSelect, "\"TIPO_LINEA\" = '0'")
        except:
            pass
        try:
            arcpy.Delete_management(feature, "FeatureClass")
        except:
            pass
    except Exception, e:
        print  e.message
        print arcpy.GetMessages()


#    try:
#        print"creando feature de linea fase 2", feature
#        arcpy.XYToLine_management(TBL_XYLINE_TableSelect,feature, "X1", "Y1", "X2", "Y2", "GEODESIC", "", "PROJCS['WGS_1984_UTM_Zone_15N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-93.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]];-5120900 -9998100 10000;-100000 10000;-100000 10000;0,001;0,001;0,001;IsHighPrecision")
#    except Exception, e:
#        print  "creando xy",feature
#        print  e.message
#        print arcpy.GetMessages()





#main()


Carga_postes()
#print" inicianda parte 1" 
#Arch = open("LINEASXY0.csv","w")#abre archivo tmp a trabajar
#Arch.write('MSLINK,X1,Y1,X2,Y2,TIPO_LINEA,POSTE1,POSTE2\n')
#print "cargando alta tension"
#Linea_mslink('select distinct mslink from conductor_trasmision order by mslink',0)
#print "cargando media tension"
#Linea_mslink('select distinct mslink from conductor_primario order by mslink',1 )
#print "cargando baja tension"
#Linea_mslink('select distinct mslink from conductor_secundario order by mslink',2 )
#Arch.close()
print "insertando a tabla"
inserta_tabla(r'LINEASXY0.csv')
#inserta_tabla(r'LINEASXY1.csv')
#inserta_tabla(r'LINEASXY2.csv')



print "game over, have a nice day!"
time.sleep(500)

#print "cargando features"
#crea_puntos_lineas()
#print "terminanda parte 1" 

#################################################################################################################################################################
################################################################################################################################################################