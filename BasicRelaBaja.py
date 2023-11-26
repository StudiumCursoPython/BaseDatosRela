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
        conn.commit()

        print(f"Alumno con ID {nombre} eliminado correctamente.")

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
        
        # Consulta SQL para eliminar un alumno
        sql = "DELETE FROM profesores WHERE id_profesor = %s"
        valores = (id_profesor,)

        # Ejecutar la consulta
        cursor.execute(sql, valores)
        conn.commit()

        print(f"Alumno con ID {id_profesor} eliminado correctamente.")

    except mysql.connector.Error as e:
        print(f"Error al eliminar el profesor: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Eliminar el alumno con nombre ...
eliminar_alumno("Alumno2")

eliminar_profesor("2")
