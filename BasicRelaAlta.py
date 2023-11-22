import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Studium2020;",
        database="CursoPy"
    )

def insertar_profesor(nombre, apellidos, edad, ciudad):
    try:
        conn = conectar()
        cursor = conn.cursor()
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
for i in range(1, 12):
    insertar_alumno(f"Alumno{i}", "Apellido", 20 + i, "Ciudad", id_profesor)
