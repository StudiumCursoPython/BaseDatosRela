import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Studium2020;",
        database="CursoPy"
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

# Eliminar el alumno con nombre ...
eliminar_alumno("Alumno2")
