import tkinter as tk
from tkinter import messagebox

### Funciones de los botones
def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    messagebox.showinfo("Inicio de sesión", f"Usuario: {usuario}\nContraseña: {contrasena}")

def registrarse():
    messagebox.showinfo("Registro", "Función de registro aún no implementada.")

def registrar_paciente():
    messagebox.showinfo("Registro Paciente", "Función de registrar paciente aún no implementada.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Login - Sistema hospitalario")
ventana.geometry("400x350")
ventana.configure(bg="#BBBBBB")  # fondo gris claro

# Colores
color_azul = "#1f77b4"
color_blanco = "#ffffff"
color_gris = "#EDEDED"

# Etiqueta de título
titulo = tk.Label(ventana, text="Sistema Hospitalario", font=("Helvetica", 16, "bold"), bg=color_gris, fg=color_azul)
titulo.pack(pady=20)

# Marco de formulario
frame = tk.Frame(ventana, bg=color_blanco, bd=2, relief="groove")
frame.pack(padx=30, pady=10)

# Campo de usuario
label_usuario = tk.Label(frame, text="Nombre de usuario:", bg=color_blanco)
label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_usuario = tk.Entry(frame, width=25)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)

# Campo de contraseña
label_contrasena = tk.Label(frame, text="Contraseña:", bg=color_blanco)
label_contrasena.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_contrasena = tk.Entry(frame, show="*", width=25)
entry_contrasena.grid(row=1, column=1, padx=10, pady=10)

# Botones
boton_login = tk.Button(ventana, text="Iniciar sesión", bg=color_azul, fg=color_blanco, width=20, command=iniciar_sesion)
boton_login.pack(pady=10)

boton_registro = tk.Button(ventana, text="Registrarse", bg=color_gris, width=20, command=registrarse)
boton_registro.pack()

boton_reg_paciente = tk.Button(ventana, text="Registrar paciente", bg=color_gris, width=20, command=registrar_paciente)
boton_reg_paciente.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
