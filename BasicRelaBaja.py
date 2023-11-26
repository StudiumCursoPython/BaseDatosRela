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

def eliminar_alumno(nombre):
    try:
        conn = conectar()
        cursor = conn.cursor()
        
        # Consulta SQL para eliminar un alumno
        sql = "DELETE FROM alumnos WHERE nombre = %s"
        valores = (nombre,)

        # Ejecutar la consulta
        cursor.execute(sql, valores)

        print(f"Alumno con nombre {nombre} eliminado correctamente.")

        conn.commit()

    except mysql.connector.Error as e:
        print(f"Error al eliminar el alumno: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def eliminar_profesor(id_profesor):
    try:
        conn = conectar()
        cursor = conn.cursor()
        
        # Consulta SQL para eliminar los alumnos asociados a este profesor
        sql_eliminar_alumnos = "DELETE FROM alumnos WHERE id_profesor = %s"
        valores_alumnos = (id_profesor,)

        # Ejecutar la consulta para eliminar los alumnos
        cursor.execute(sql_eliminar_alumnos, valores_alumnos)
        
        # Consulta SQL para eliminar al profesor
        sql_eliminar_profesor = "DELETE FROM profesores WHERE id_profesor = %s"
        valores_profesor = (id_profesor,)

        # Ejecutar la consulta para eliminar al profesor
        cursor.execute(sql_eliminar_profesor, valores_profesor)

        print(f"Profesor con ID {id_profesor} eliminado correctamente.")

        conn.commit()  

    except mysql.connector.Error as e:
        print(f"Error al eliminar el profesor: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Ejemplo para eliminar un profesor por su ID, cambiar la ID según la BBDD
eliminar_profesor("3")

# Ejemplo para eliminar a un alumno por su nombre, cambiar nombre según la BBDD
eliminar_alumno("Alumno6")

