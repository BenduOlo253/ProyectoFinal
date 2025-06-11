from datos.pacienteDAO import PacienteDAO

class PacienteService:

    def __verificarDuplicados(idPaciente):
        pacientes = PacienteDAO.obtenerPacientePorId(idPaciente)
        if len(pacientes) == 0:
            return False
        else: return True

    @staticmethod
    def obtenerPacientes():
        return PacienteDAO.obtenerPacientes()
    
    @staticmethod
    def buscarPaciente(idPaciente):
        return (PacienteDAO.obtenerPacientePorId(idPaciente))[0]

    @staticmethod
    def registrarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido):
        if PacienteService.__verificarDuplicados(idPaciente):
            PacienteDAO.insertarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido)
        else:
            raise ValueError("El ID del paciente ya existe. Por favor, use un ID único.")
        
    @staticmethod
    def actualizarPaciente(nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido, idPaciente):
        PacienteDAO.actualizarPaciente(nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido, idPaciente)
        return (f"El paciente {nombre} ha sido actualizado correctamente.")
    
    @staticmethod
    def removerPaciente(idPaciente):
        PacienteDAO.eliminarPaciente(idPaciente)
        return "El paciente ha sido eliminado correctamente."