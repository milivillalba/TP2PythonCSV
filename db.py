# import sys
import MySQLdb
import csv

# Conexión a la base de datos
try:
    db = MySQLdb.connect("localhost", "root", "", "tpcsv")
    print("Conexión establecida correctamente.")
    cursor = db.cursor()

    # Leer datos del archivo CSV y cargar en la tabla
    def lectura_csv():
        try:
            with open('localidades.csv', newline='') as archivo_csv:
                lector_csv = csv.reader(archivo_csv, delimiter=',', quotechar='"')
                return list(lector_csv)
        except FileNotFoundError as e:
            print(f'No se pudo abrir el archivo. Error: {e}')
            return []

    # Borrar la tabla si existe
    cursor.execute("DROP TABLE IF EXISTS consulta_localidad_provincia")
    print("Tabla eliminada si existía.")

    # Crear tabla en la base de datos MySQL
    cursor.execute("CREATE TABLE consulta_localidad_provincia (provincia VARCHAR(200), id INT, localidad VARCHAR(200), cp VARCHAR(200), id_prov_mstr VARCHAR(200))")
    print("Tabla creada correctamente.")

    # Insertar datos en la tabla
    try:
        rows_to_insert = lectura_csv()
        if rows_to_insert:
            for row in rows_to_insert:
                try:
                    cursor.execute("INSERT INTO consulta_localidad_provincia (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)", row)
                except MySQLdb.Error as e:
                    print(f"Error al insertar fila {row}: {e}")
                    db.rollback()
                    continue
            db.commit()
            print("Todos los datos insertados correctamente en la BD.")
        else:
            print("No hay datos para insertar.")
    except Exception as e:
        print(f"Error durante la inserción de datos: {e}")

except MySQLdb.Error as e:
    print("No se pudo conectar a la base de datos:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
finally:
    if 'db' in locals() and db:
        db.close()
        print("Conexión cerrada.")

