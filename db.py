import sys
import MySQLdb

#conexion a la base de datos 
try:
    db= MySQLdb.connect("localhost","root","","tpcsv")
except MySQLdb.Error as e:
    print("No se pudo conectar a la base de datos:",e)
    sys.exit(1)
print("Conexion correcta.")

cursor= db.close()
#Borrar la tAbla



