import mysql.connector
from mysql.connector import Error
class DataBase:
    try:
        conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='lentes',
        )
    
        if conexion.is_connected():
            print("Conexión exitosa")
            cursor=conexion.cursor()
            nombre=input("ingrese el nombre del usuario: ")
            documento=input("ingrese el documento del usuario: ")
            direccion=input("ingrese la direccion del usuario: ")
            mail=input("ingrese el mail: ")
            sentencia="INSERT INTO alumno (nombre,documento,domicilio,mail) VALUES (%s,%s,%s,%s)"
            val=(nombre, documento, direccion, mail)
            
            cursor.execute(sentencia, val)
            conexion.commit()
            print("registro realizado con exito")
    except Error as ex:
        print("Error durante la conexion:",ex)
    finally:
        if conexion.is_connected():
            conexion.close()
            print("La conexión ha finalizado")

