from tkinter import simpledialog
from tkinter import *
import tkinter as tk
import mysql.connector
import os
import sys

def conectar():
    return mysql.connector.connect(
        host="178.211.133.56",
        user="ofluqcym_cursoFor",
        password="Studium2020;",
        database="ofluqcym_CursoPy"
    )

def eliminar_profesor():
    id_profesor = simpledialog.askstring("Eliminar Profesor", "Ingrese el ID del profesor:")
    if id_profesor:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM profesores WHERE id_profesor = %s", (id_profesor,))
        conexion.commit()
        conexion.close()

def eliminar_alumno():
    id_alumno = simpledialog.askstring("Eliminar Alumno", "Ingrese el ID del alumno:")
    if id_alumno:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM alumnos WHERE id_alumno = %s", (id_alumno,))
        conexion.commit()
        conexion.close()

root = tk.Tk()
root.title("Bajas de P. y A.")
root.geometry("300x70")

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Crear la ventana de la aplicación
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

boton_profesor = tk.Button(root, text="Eliminar Profesor", command=eliminar_profesor)
boton_profesor.pack()

boton_alumno = tk.Button(root, text="Eliminar Alumno", command=eliminar_alumno)
boton_alumno.pack()

root.iconphoto(True,icono)
root.mainloop()

