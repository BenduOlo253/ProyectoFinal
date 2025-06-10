# Clase que representa a un paciente con atributos básicos
class Usuario:
    def __init__(self, idUsuario, nombre, contraseña, rol):
        self.__idUsuario = idUsuario                 # Identificador único del usuario, puede ser su numero de trabajador.
        self.__nombre = nombre         # Nombre del usuario.
        self.__contraseña = contraseña # Contraseña del usuario.
        self.__rol = rol              # Rol del usuario (por ejemplo, 'admin', 'doctor', 'enfermero', etc.).
    
    # Getters
    def getId(self):
        return self.__idUsuario
    
    def getNombre(self):
        return self.__nombre
    
    def getContraseña(self):
        return self.__contraseña
    
    def getRol(self):
        return self.__rol


    # Setters        
    def setId(self, idUsuario):
        self.__idUsuario = idUsuario
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setContraseña(self, contraseña):
        self.__contraseña = contraseña
    def setRol(self, rol):
        self.__rol = rol

    # Método para representar el objeto como una cadena de texto.
    def __str__(self):
        return f"Usuario(idUsuario:{self.__idUsuario}, nombre:{self.__nombre}, rol={self.__rol})"