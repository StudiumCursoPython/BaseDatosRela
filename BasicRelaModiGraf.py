""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from tkinter import messagebox, Tk, PhotoImage
import  tkinter as tk
import os,sys
import mysql.connector

HOST = "178.211.133.56"
USER = "ofluqcym_cursoFor"
PASSWORD = "Studium2020;"
DATABASE = "ofluqcym_CursoPy"


def conectar():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

def modificar_alumno(id_alumno, nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad):
    if not all([id_alumno, nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad]):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return False

    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = """
        UPDATE alumnos
        SET nombre = %s, apellidos = %s, edad = %s, ciudad = %s
        WHERE id_alumno = %s
        """
        valores = (nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad, id_alumno)

        cursor.execute(sql, valores)
        conn.commit()

        if cursor.rowcount == 0:
            return False

        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al modificar el alumno: {str(e)}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def modificar_profesor(id_profesor, nuevo_nombre, nuevo_apellido, nueva_edad, nueva_ciudad):
    if not all([id_profesor, nuevo_nombre, nuevo_apellido, nueva_edad, nueva_ciudad]):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return False
    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = """
        UPDATE profesores
        SET nombre = %s, apellidos = %s, edad = %s, ciudad = %s
        WHERE id_profesor = %s
        """
        valores = (nuevo_nombre, nuevo_apellido, nueva_edad, nueva_ciudad, id_profesor)

        cursor.execute(sql, valores)
        conn.commit()

        if cursor.rowcount == 0:
            return False

        return True
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al modificar el profesor: {str(e)}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def interfaz_modificar_profesor():
    id_profesor = entrada_id_profesor.get()
    nuevo_nombre = entrada_nombre_profesor.get()
    nuevo_apellido = entrada_apellidos_profesor.get()
    nueva_edad = entrada_edad_profesor.get()
    nueva_ciudad = entrada_ciudad_profesor.get()

    if modificar_profesor(id_profesor, nuevo_nombre, nuevo_apellido, nueva_edad, nueva_ciudad):
        messagebox.showinfo("Éxito", "Profesor modificado con éxito")
        borrado_campos()
    else:
        messagebox.showerror("Error", "No se pudo modificar el profesor")
        borrado_campos()

def interfaz_modificar_alumno():
    id_alumno = entrada_id_alumno.get()
    nuevo_nombre = entrada_nombre_alumno.get()
    nuevos_apellidos = entrada_apellidos_alumno.get()
    nueva_edad = entrada_edad_alumno.get()
    nueva_ciudad = entrada_ciudad_alumno.get()

    if modificar_alumno(id_alumno, nuevo_nombre, nuevos_apellidos, nueva_edad, nueva_ciudad):
        messagebox.showinfo("Éxito", "Alumno modificado con éxito")
        borrado_campos()
    else:
        messagebox.showerror("Error", "No se pudo modificar el alumno")
        borrado_campos()

def borrado_campos():
    entrada_nombre_profesor.delete(0, 'end')
    entrada_apellidos_profesor.delete(0, 'end')
    entrada_edad_profesor.delete(0, 'end')
    entrada_ciudad_profesor.delete(0, 'end')
    entrada_id_profesor.delete(0, 'end')
    # De alumnos
    entrada_nombre_alumno.delete(0, 'end')
    entrada_apellidos_alumno.delete(0, 'end')
    entrada_edad_alumno.delete(0, 'end')
    entrada_ciudad_alumno.delete(0, 'end')
    entrada_id_alumno.delete(0, 'end')

aplicacion = Tk()
aplicacion.title("Modificaciones P. y A.")
aplicacion.geometry("250x320")
# centrado aproximado de la ventana
aplicacion.eval('tk::PlaceWindow . center')
aplicacion.resizable(False, False)

ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

# Campos de entrada y botones para profesores
tk.Label(aplicacion, text="ID Profesor:").grid(row=0, column=0)
entrada_id_profesor = tk.Entry(aplicacion)
entrada_id_profesor.grid(row=0, column=1)

tk.Label(aplicacion, text="Nombre Profesor:").grid(row=1, column=0)
entrada_nombre_profesor = tk.Entry(aplicacion)
entrada_nombre_profesor.grid(row=1, column=1)

tk.Label(aplicacion, text="Apellidos Profesor:").grid(row=2, column=0)
entrada_apellidos_profesor = tk.Entry(aplicacion)
entrada_apellidos_profesor.grid(row=2, column=1)

tk.Label(aplicacion, text="Edad Profesor:").grid(row=3, column=0)
entrada_edad_profesor = tk.Entry(aplicacion)
entrada_edad_profesor.grid(row=3, column=1)

tk.Label(aplicacion, text="Ciudad Profesor:").grid(row=4, column=0)
entrada_ciudad_profesor = tk.Entry(aplicacion)
entrada_ciudad_profesor.grid(row=4, column=1)

tk.Button(aplicacion, text="Modificar Profesor", command=interfaz_modificar_profesor).grid(row=5, column=0, columnspan=2)

# Campos de entrada y botones para alumnos
tk.Label(aplicacion, text="ID Alumno:").grid(row=6, column=0)
entrada_id_alumno = tk.Entry(aplicacion)
entrada_id_alumno.grid(row=6, column=1)

tk.Label(aplicacion, text="Nombre Alumno:").grid(row=7, column=0)
entrada_nombre_alumno = tk.Entry(aplicacion)
entrada_nombre_alumno.grid(row=7, column=1)

tk.Label(aplicacion, text="Apellidos Alumno:").grid(row=8, column=0)
entrada_apellidos_alumno = tk.Entry(aplicacion)
entrada_apellidos_alumno.grid(row=8, column=1)

tk.Label(aplicacion, text="Edad Alumno:").grid(row=9, column=0)
entrada_edad_alumno = tk.Entry(aplicacion)
entrada_edad_alumno.grid(row=9, column=1)

tk.Label(aplicacion, text="Ciudad Alumno:").grid(row=10, column=0)
entrada_ciudad_alumno = tk.Entry(aplicacion)
entrada_ciudad_alumno.grid(row=10, column=1)

tk.Button(aplicacion, text="Modificar Alumno", command=interfaz_modificar_alumno).grid(row=11, column=0, columnspan=2)
tk.Button(aplicacion, text = "Borrar campos", command=borrado_campos).grid(row=12, column=0, columnspan=2)
tk.Label(aplicacion, text ="*Todos los campos son obligatorios").grid(row=13, column=0, columnspan=2)

aplicacion.iconphoto(True, icono)
aplicacion.mainloop()

