# Clase que representa a un paciente con atributos básicos
class Paciente:
    def __init__(self, id, nombre, edad, gravedad):
        self.id = id                # Identificador único del paciente
        self.nombre = nombre        # Nombre del paciente
        self.edad = edad            # Edad del paciente
        self.gravedad = gravedad    # Nivel de gravedad (prioridad): entre más alto, más urgente
