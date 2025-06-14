from Modelo.servicio.pacienteService import PacienteService
from tkinter import messagebox

class ListaPacientesControlador:
    @staticmethod
    def obtenerPacientesListaSimple():
        # Supongamos que PacienteService.verPacientesPorGravedad() devuelve lista de objetos Paciente,
        # y cada Paciente tiene métodos o atributos: id, nombre, edad, genero, motivo, gravedad, fechaIngreso, atendido.

        pacientes_obj = PacienteService.verPacientesPorGravedad()

        if not pacientes_obj:
            messagebox.showinfo("Información", "No hay pacientes registrados.")
            return []

        lista_simple = []
        for paciente in pacientes_obj:
            # Aquí extraemos atributos, asegurando que sea lista simple sin diccionarios ni estructuras avanzadas
            fila = [
                getattr(paciente, "idPaciente", ""),
                getattr(paciente, "nombre", ""),
                str(getattr(paciente, "edad", "")),
                getattr(paciente, "genero", ""),
                getattr(paciente, "motivo", ""),
                getattr(paciente, "gravedad", ""),
                getattr(paciente, "fechaIngreso", ""),
                "Sí" if getattr(paciente, "atendido", False) else "No"
            ]
            lista_simple.append(fila)
        
        return lista_simple
