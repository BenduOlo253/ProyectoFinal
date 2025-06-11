from Modelo.servicio.pacienteService import PacienteService
from Modelo.servicio.usuarioService import UsuarioService
from 

def determinarVentana(caso):
    
    if caso == "login":
        return











### Funciones de los botones
def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    messagebox.showinfo("Inicio de sesión", f"Usuario: {usuario}\nContraseña: {contrasena}")

def registrarse():
    messagebox.showinfo("Registro", "Función de registro aún no implementada.")