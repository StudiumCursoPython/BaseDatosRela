"""
Curso Python empresa

Autor: José Antonio Calvo López
Fecha: Noviembre de 2023
"""

from mysql.connector import Error
import mysql.connector

HOST = "178.211.133.56"
USER = "ofluqcym_cursoFor"
PASSWORD = "Studium2020;"
DATABASE = "ofluqcym_CursoPy"

def conectar():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

def probar_conexion():
    try:
        conexion = conectar()
        if conexion.is_connected():
            db_Info = conexion.get_server_info()
            print("Conectado a MySQL Server versión ", db_Info)
            cursor = conexion.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a la base de datos: ", record)
            
        cursor.close()
        conexion.close()
        print("La conexión a MySQL se ha cerrado")

    except Error as e:
        print("Error al conectar a MySQL", e)

probar_conexion()