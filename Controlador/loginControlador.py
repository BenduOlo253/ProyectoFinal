from Modelo.servicio.usuarioService import UsuarioService
from tkinter import messagebox
import tkinter as tk

class LoginControlador:
    def __init__(self):
        self.usuarioService = UsuarioService()

    def iniciar_sesion(self, idUsuario, contraseña):
        if self.usuarioService.autenticarUsuario(idUsuario, contraseña):
            usuario = self.usuarioService.buscarUsuario(idUsuario)
            if usuario:
                nombreUsuario = usuario.getNombre()
                messagebox.showinfo("Inicio de sesión exitoso!", f"Bienvenido {nombreUsuario}!")
                from Vista.Vent_princ import VentanaPrincipal
                VentanaPrincipal(tk.Tk(), nombreUsuario).mostrar()
            else:
                messagebox.showerror("Error", "Usuario no encontrado después de autenticar.")
        else:
            from Vista.vent_login import Login
            Login(tk.Tk()).mostrar()
            messagebox.showerror("Error de inicio de sesión", "ID de usuario o contraseña incorrectos.")

    def registrarUsuario(self, id_usuario, nombre, contraseña, rol):
        if not id_usuario or not nombre or not contraseña or not rol:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        mensaje = self.usuarioService.registrarUsuario(id_usuario, nombre, contraseña, rol)
        messagebox.showinfo("Información sobre registro", mensaje)
