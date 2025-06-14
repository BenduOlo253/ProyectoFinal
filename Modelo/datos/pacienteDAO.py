from Modelo.dominio.Paciente import Paciente
from structures.tablaHash import TablaHash
from structures.listaEnlazada import ListaEnlazada

class PacienteDAO:
    def __init__(self):
        self.tabla = TablaHash()

    def guardar(self, paciente: Paciente):
        clave = paciente.getIdPaciente()
        self.tabla.insertarValor(clave, paciente)

    def obtener_por_id(self, idPaciente):
        return self.tabla.obtenerValor(idPaciente)

    def eliminar(self, idPaciente):
        return self.tabla.eliminarValor(idPaciente)
    
    def obtenerPacientes(self):
        pacientes = ListaEnlazada()
        for listadoPacientes in self.tabla.tabla:
            for paciente in listadoPacientes:
                pacientes.insertar(paciente.getIdPaciente(), paciente)
        return pacientes
