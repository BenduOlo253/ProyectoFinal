from Modelo.servicio.pacienteService import PacienteService
from Modelo.servicio.usuarioService import UsuarioService
from tkinter import messagebox

class VentPrincipalControlador:
    def __init__(self):
        self.pacienteService = PacienteService()
        self.usuarioService = UsuarioService()

    def registrarPaciente(self, idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido):
        if not idPaciente or not nombre or not edad or not genero or not motivo or not gravedad or not fechadeingreso:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return
        mensaje = self.pacienteService.registrarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido)
        messagebox.showinfo("Información sobre registro", mensaje)
