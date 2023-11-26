from tkinter import messagebox
from tkinter import *
import tkinter as tk
import mysql.connector
import os
import sys

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
        return cursor.lastrowid
    except mysql.connector.Error as e:
        print(f"Error al insertar profesor: {e}")
        return None
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
        return True
    except mysql.connector.Error as e:
        print(f"Error al insertar alumno: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def interfaz_insertar_profesor():
    nombre_profesor = entrada_nombre_profesor.get()
    apellidos_profesor = entrada_apellidos_profesor.get()
    edad_profesor = int(entrada_edad_profesor.get())  
    ciudad_profesor = entrada_ciudad_profesor.get()
    id_profesor = insertar_profesor(nombre_profesor, apellidos_profesor, edad_profesor, ciudad_profesor)
    
    if id_profesor is not None:
        messagebox.showinfo("Éxito", "Profesor insertado con éxito")
    else:
        messagebox.showerror("Error", "No se pudo insertar el profesor")

def interfaz_insertar_alumno():
    nombre_alumno = entrada_nombre_alumno.get()
    apellidos_alumno = entrada_apellidos_alumno.get()
    edad_alumno = int(entrada_edad_alumno.get())  
    ciudad_alumno = entrada_ciudad_alumno.get()
    id_profesor = int(entrada_id_profesor.get())  

    exito = insertar_alumno(nombre_alumno, apellidos_alumno, edad_alumno, ciudad_alumno, id_profesor)
    
    if exito:
        messagebox.showinfo("Éxito", "Alumno insertado con éxito")
    else:
        messagebox.showerror("Error", "No se pudo insertar el alumno")

# Crear la ventana principal
aplicacion = tk.Tk()
aplicacion.title("Altas de P y A")
aplicacion.geometry("350x270")
aplicacion.resizable(False, False)

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Crear la ventana de la aplicación
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

# Crear y colocar los campos y botones para insertar profesores
tk.Label(aplicacion, text="Nombre Profesor:").grid(row=0, column=0)
entrada_nombre_profesor = tk.Entry(aplicacion)
entrada_nombre_profesor.grid(row=0, column=1)

tk.Label(aplicacion, text="Apellidos Profesor:").grid(row=1, column=0)
entrada_apellidos_profesor = tk.Entry(aplicacion)
entrada_apellidos_profesor.grid(row=1, column=1)

tk.Label(aplicacion, text="Edad Profesor:").grid(row=2, column=0)
entrada_edad_profesor = tk.Entry(aplicacion)
entrada_edad_profesor.grid(row=2, column=1)

tk.Label(aplicacion, text="Ciudad Profesor:").grid(row=3, column=0)
entrada_ciudad_profesor = tk.Entry(aplicacion)
entrada_ciudad_profesor.grid(row=3, column=1)

tk.Button(aplicacion, text="Insertar Profesor", command=interfaz_insertar_profesor).grid(row=4, column=0, columnspan=2)

# Crear y colocar los campos y botones para insertar alumnos
tk.Label(aplicacion, text="Nombre Alumno:").grid(row=5, column=0)
entrada_nombre_alumno = tk.Entry(aplicacion)
entrada_nombre_alumno.grid(row=5, column=1)

tk.Label(aplicacion, text="Apellidos Alumno:").grid(row=6, column=0)
entrada_apellidos_alumno = tk.Entry(aplicacion)
entrada_apellidos_alumno.grid(row=6, column=1)

tk.Label(aplicacion, text="Edad Alumno:").grid(row=7, column=0)
entrada_edad_alumno = tk.Entry(aplicacion)
entrada_edad_alumno.grid(row=7, column=1)

tk.Label(aplicacion, text="Ciudad Alumno:").grid(row=8, column=0)
entrada_ciudad_alumno = tk.Entry(aplicacion)
entrada_ciudad_alumno.grid(row=8, column=1)

tk.Label(aplicacion, text="ID Profesor:").grid(row=9, column=0)
entrada_id_profesor = tk.Entry(aplicacion)
entrada_id_profesor.grid(row=9, column=1)

tk.Button(aplicacion, text="Insertar Alumno", command=interfaz_insertar_alumno).grid(row=10, column=0, columnspan=2)

Label(aplicacion, text="*Todos los campos son requeridos").grid(row=11, column=0)

# Mostrar la ventana
aplicacion.iconphoto(True, icono)
aplicacion.mainloop()
