import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=.;"
                      "Database=Locottus;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM t1')

for row in cursor:
    print('row = %r' % (row,))



