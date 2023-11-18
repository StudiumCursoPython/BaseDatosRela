import mysql.connector

# Conexión a la base de datos MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",  
        user="root", 
        password="Studium2020;",
        database="CursoPy"
    )
    cursor = conn.cursor()

    # Ejecución de la consulta en mysql
    cursor.execute("SELECT nombre FROM alumnos")

    # Recuperación de los datos
    nombres_alumnos = cursor.fetchall()

    # Para ver los resultados
    for nombre in nombres_alumnos:
        print(nombre[0])

except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")
    
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión a MySQL cerrada")

