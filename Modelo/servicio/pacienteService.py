from Modelo.datos.pacienteDAO import PacienteDAO
from Modelo.dominio.Paciente import Paciente
from Utils.sorting import merge_sort

class PacienteService:
    def __init__(self):
        self.pacienteDAO = PacienteDAO()

    def __verificarDuplicados(self, idPaciente):
        paciente = self.pacienteDAO.obtener_por_id(idPaciente)
        return paciente is not None

    def obtenerPacientes(self):
        return self.pacienteDAO.obtenerPacientes()  # Devuelve ListaEnlazada

    def obtenerPacientesPorGravedad(self):
        pacientes_lista = []
        pacientes = self.obtenerPacientes()
        # Convertir ListaEnlazada a lista normal para ordenar
        nodo = pacientes.cabeza
        while nodo:
            pacientes_lista.append(nodo.valor)
            nodo = nodo.siguiente
        # Ordenar con merge_sort según gravedad (descendente)
        pacientes_ordenados = merge_sort(pacientes_lista, clave="gravedad")
        # Retornar lista ordenada (puedes convertir a ListaEnlazada si quieres)
        return pacientes_ordenados

    def buscarPaciente(self, idPaciente):
        return self.pacienteDAO.obtener_por_id(idPaciente)

    def registrarPaciente(self, idPaciente, nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido):
        if not self.__verificarDuplicados(idPaciente):
            paciente = Paciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido)
            self.pacienteDAO.guardar(paciente)
            return f"El paciente {nombre} ha sido registrado correctamente."
        else:
            return "El ID del paciente ya existe. Por favor, use un ID único."

    def actualizarPaciente(self, idPaciente, nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido):
        paciente = self.pacienteDAO.obtener_por_id(idPaciente)
        if paciente:
            paciente.setNombre(nombre)
            paciente.setEdad(edad)
            paciente.setGenero(genero)
            paciente.setMotivo(motivo)
            paciente.setGravedad(gravedad)
            paciente.setFechaIngreso(fechaDeIngreso)
            paciente.setAtendido(atendido)
            self.pacienteDAO.guardar(paciente)  # Reemplaza el existente
            return f"El paciente {nombre} ha sido actualizado correctamente."
        else:
            return "Paciente no encontrado."

    def removerPaciente(self, idPaciente):
        eliminado = self.pacienteDAO.eliminar(idPaciente)
        if eliminado:
            return "El paciente ha sido eliminado correctamente."
        else:
            return "Paciente no encontrado."
