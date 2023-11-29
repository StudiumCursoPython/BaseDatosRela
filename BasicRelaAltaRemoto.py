import mysql.connector

HOST = "178.211.133.56"
USER = "ofluqcym_cursoFor"
PASSWORD = "Studium2020;"
DATABASE = "ofluqcym_CursoPy"


def conectar():
    return mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE
    )

def insertar_profesor(nombre, apellidos, edad, ciudad):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO profesores (nombre, apellidos, edad, ciudad) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellidos, edad, ciudad)
        cursor.execute(sql, valores)
        conn.commit()
        # En este caso no se usa, se muestra para que se vea como se puede recupar una ID autoincrement.
        return cursor.lastrowid
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def insertar_alumno(nombre, apellidos, edad, ciudad, id_profesor):
    try:
        conn = conectar()
        cursor = conn.cursor()
        sql = "INSERT INTO alumnos (nombre, apellidos, edad, ciudad, id_profesor) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, apellidos, edad, ciudad, id_profesor)
        cursor.execute(sql, valores)
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Inserta en la tabla profesor
id_profesor = insertar_profesor("José Antonio", "Calvo López", 53, "Sevilla")

# Se inserta a 11 alumnos con bucle for
for i in range(1, 12):
    insertar_alumno(f"Alumno{i}", "Apellido", 20 + i, "Ciudad", id_profesor)
