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

def modificar_alumno(id_alumno, nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad):
    try:
        conn = conectar()
        cursor = conn.cursor()

        # Consulta SQL para modificar un alumno
        # Tres comillas triples, permiten que la consulta se escriba en varias líneas para mejorar la legibilidad
        sql = """
        UPDATE alumnos
        SET nombre = %s, apellidos = %s, edad = %s, ciudad = %s
        WHERE id_alumno = %s
        """
        valores = (nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad, id_alumno)

        # Ejecutar la consulta
        cursor.execute(sql, valores)
        conn.commit()

        print("Alumno con ID " + str(id_alumno) + " modificado correctamente.") #Concatenación anteriror a f-strings

    except mysql.connector.Error as e:
        print(f"Error al modificar el alumno: {e}" + e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Modificar Profesor

def modificar_profesor(id_profesor, nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad):
    try:
        conn = conectar()
        cursor = conn.cursor()

        # Consulta SQL para modificar al profesor
        sql = """
        UPDATE profesores
        SET nombre = %s, apellidos = %s, edad = %s, ciudad = %s
        WHERE id_profesor = %s
        """
        valores = (nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad, id_profesor)

        # Ejecutar la consulta
        cursor.execute(sql, valores)
        conn.commit()

        print("Profesor con ID " + str(id_profesor) + " modificado correctamente.") #Concatenación anteriror a f-strings

    except mysql.connector.Error as e:
        print(f"Error al modificar al profesor: {e}" + e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



# El Alumno con id_alumno34 va a modificar los datos que se pasan por parámentros al método, asegurarse que existe la id
# Si no existen las id respectivas lo dará por cambiado.
modificar_alumno(34, "Antonio", "García", 39, "Palmete")

modificar_profesor(5, "José Andrés", "Marín Huertas", 53, "Cadiz")
