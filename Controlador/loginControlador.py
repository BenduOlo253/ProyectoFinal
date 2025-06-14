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

    def registrarUsuario(id_usuario, nombre, contraseña, rol):
        if not id_usuario or not nombre or not contraseña or not rol:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        messagebox.showinfo("Informacion sobre registro", UsuarioService.registrarUsuario(id_usuario, nombre, contraseña, rol))

        