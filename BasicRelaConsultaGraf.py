""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

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

def consultar_alumnos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM alumnos")
        datos_alumnos = cursor.fetchall()
        # Para limpiar el area del texto
        area_texto.delete(1.0, tk.END)
        for alumno in datos_alumnos:
            area_texto.insert(tk.END, str(alumno) + "\n")
    
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al conectar a MySQL: {str(e)}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def consultar_profesores():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profesores")
        datos_profesores = cursor.fetchall()
        # Para limpiar el area del texto
        area_texto.delete(1.0, tk.END)  
        for profesor in datos_profesores:
            area_texto.insert(tk.END, str(profesor) + "\n")
    
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al conectar a MySQL: {str(e)}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

root = tk.Tk()
root.title("Consulta BBDD")
#centrado aproximado de la ventana
root.eval('tk::PlaceWindow . center')
root.geometry("420x240")
root.resizable(False,False)

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Crear la ventana de la aplicación
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))
# Creación de un marco para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para consultar alumnos, colocado en el marco
boton_alumno = tk.Button(frame_botones, text="Consulta de alumnos", command=consultar_alumnos)
boton_alumno.pack(side=tk.LEFT, padx=10)

# Botón para consultar profesores, colocado en el marco
boton_profesor = tk.Button(frame_botones, text="Consulta de profesores", command=consultar_profesores)
boton_profesor.pack(side=tk.LEFT, padx=10)

# Área de texto debajo del marco de los botones
area_texto = tk.Text(root, height=15, width=50)
area_texto.pack(pady=10)

root.iconphoto(True,icono)
root.mainloop()
