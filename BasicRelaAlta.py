import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "Studium2020;"
DATABASE = "CursoPy"

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
         # El simbolo %s es un marcador de posición se usa independientemente del tipo de datos
        sql = "INSERT INTO profesores (nombre, apellidos, edad, ciudad) VALUES (%s, %s, %s, %s)"
        valores = (nombre, apellidos, edad, ciudad)
        cursor.execute(sql, valores)
        conn.commit()
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
        # El simbolo % es un marcador de posición se usa independientemente del tipo de datos
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
id_profesor = insertar_profesor("José Manuel", "Marín López", 53, "Sevilla")

# Se inserta a 11 alumnos con bucle for
for i in range(1, 3):
    insertar_alumno(f"Alumno{i}", "Apellido", 20 + i, "Ciudad", id_profesor)
