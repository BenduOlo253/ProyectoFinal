# Clase que representa a un paciente con atributos básicos
class Paciente:
    def __init__(self, idPaciente, nombre, edad, genero, motivo, gravedad, fechaIngreso):
        self.__idPaciente = idPaciente
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
        self.__motivo = motivo
        self.__gravedad = gravedad
        self.__feechaIngreso = fechaIngreso