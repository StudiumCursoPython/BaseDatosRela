import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = "Studium2020;"
DATABASE = "CursoPy"

# Conexión a la base de datos MySQL
try:
    conn = mysql.connector.connect(
        host = HOST,  
        user = USER, 
        password = PASSWORD,
        database = DATABASE
    )
    cursor = conn.cursor()

    # Ejecución de la consulta en mysql
    cursor.execute("SELECT nombre FROM alumnos")

    # Recuperación de los datos
    nombres_alumnos = cursor.fetchall()

    # Para ver los resultados
    for nombre in nombres_alumnos:
        # Coge la primera posicion es más correcta
        print(nombre[0])
        # Ver la diferencia
        print(nombre)
        
    cursor.execute("SELECT * FROM profesores")

    # Recuperación de los datos
    datos_profesores = cursor.fetchall()

    # Para ver los resultados
    for profesor in datos_profesores:
        print(profesor)  # Muestra todos los datos de cada profesor

except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")
    
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión a MySQL cerrada")

