from Modelo.servicio.pacienteService import PacienteService
from Modelo.servicio.usuarioService import UsuarioService
from tkinter import messagebox

class VentPrincipalControlador:
    def registrarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido):
        if not idPaciente or not nombre or not edad or not genero or not motivo or not gravedad or not fechadeingreso:
            messagebox.showerror("Error", "Todos los campor son obligatorios.")
            return
        messagebox.showinfo("Informacion sobre registro", PacienteService.registrarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido))

    def verPacientesPorGravedad():
        pacientes = PacienteService.verPacientesPorGravedad()
        if pacientes:
            pass
        else:
            messagebox.showinfo("Informacion", "No hay pacientes registrados.")
    
    def modificarUsuario():
        pass
    def verMisDatosUsuario(idUsuario):
        usuario = UsuarioService.buscarUsuario(idUsuario)
        if usuario:
            return usuario
        else:
            messagebox.showerror("Error", "Usuario no encontrado")
            
    def verPaciente(idPaciente):
        paciente = PacienteService.buscarPaciente(idPaciente)

