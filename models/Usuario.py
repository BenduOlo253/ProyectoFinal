# Clase que representa a un paciente con atributos básicos
class Usuario:
    def __init__(self, id, nombre, contraseña, rol):
        self.id = id                # Identificador único del paciente
        self.nombre = nombre        # Nombre del paciente
        self.contraseña = contraseña
        self.rol = rol
        