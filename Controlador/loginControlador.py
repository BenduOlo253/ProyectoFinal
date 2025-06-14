from Modelo.servicio.usuarioService import UsuarioService
from tkinter import messagebox
import tkinter as tk
class LoginControlador:
    ### Funciones de los botones
    def iniciar_sesion(idUsuario, contraseña):
        if UsuarioService.autenticarUsuario(idUsuario, contraseña):
            nombreUsuario = (UsuarioService.buscarUsuario(idUsuario)[0])[1]
            messagebox.showinfo("Inicio de sesion exitoso!", f"Bienvenido {nombreUsuario}!")
            from Vista.Vent_princ import VentanaPrincipal
            
            VentanaPrincipal(tk.Tk(), nombreUsuario).mostrar()
        else:
            from Vista.vent_login import Login
            Login(tk.Tk()).mostrar()
            messagebox.showerror("Error de inicio de sesión", "ID de usuario o contraseña incorrectos.")

    def registrarUsuario(id_usuario, nombre, contraseña, rol):
        if not id_usuario or not nombre or not contraseña or not rol:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        messagebox.showinfo("Informacion sobre registro", UsuarioService.registrarUsuario(id_usuario, nombre, contraseña, rol))

        