from Modelo.servicio.pacienteService import PacienteService

class RegistroPacienteControlador:
    def __init__(self):
        self.pacienteService = PacienteService()

    def registrarPaciente(self, idPaciente, nombre, edad, genero, motivo, gravedad, fechaIngreso, atendido):
        # Aquí puedes agregar más validaciones si quieres
        return self.pacienteService.registrarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechaIngreso, atendido)
