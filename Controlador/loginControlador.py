from Modelo.servicio.usuarioService import UsuarioService
from tkinter import messagebox

class LoginControlador:
    ### Funciones de los botones
    def iniciar_sesion(idUsuario, contraseña):
        if UsuarioService.autenticarUsuario(idUsuario, contraseña):
            nombreUsuario = (UsuarioService.buscarUsuario(idUsuario)[0])[1]
            messagebox.showinfo("Inicio de sesion exitoso!", f"Bienvenido {nombreUsuario}!")
        else:
            messagebox.showerror("Error de inicio de sesión", "ID de usuario o contraseña incorrectos.")

    def registrarse():
        messagebox.showinfo("Registro", "Función de registro aún no implementada.")

        