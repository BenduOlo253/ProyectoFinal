class Paciente:
    def __init__(self, idPaciente, nombre, edad, genero, motivo, gravedad, fechaIngreso, atendido):
        self.__idPaciente = idPaciente #Identificador único del paciente, en este caso es la curp del paciente.
        self.__nombre = nombre #Nombre del paciente.
        self.__edad = edad #Edad del paciente.
        self.__genero = genero # Genero del paciente(masculino, femenino).
        self.__motivo = motivo # Motivo de la consulta del paciente.
        self.__gravedad = gravedad # Gravedad del paciente(1-5).
        # 1: Muy leve, 2: Leve, 3: Moderado, 4: Grave, 5: Muy grave.
        self.__feechaIngreso = fechaIngreso # Fecha de ingreso del paciente al hospital.
        self.__atendido = atendido # Es un valor boleano que indica si el paciente ha sido atendido o no.
        
    #Geters
    def getIdPaciente(self):
        return self.__idPaciente
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getGenero(self):
        return self.__genero
    def getMotivo(self):
        return self.__motivo
    def getGravedad(self):
        return self.__gravedad
    def getFechaIngreso(self):
        return self.__feechaIngreso
    def getAtendido(self):
        return self.__atendido
    
    #Seters
    def setIdPaciente(self, idPaciente):
        self.__idPaciente = idPaciente
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setEdad(self, edad):
        self.__edad = edad
    def setGenero(self, genero):
        self.__genero = genero
    def setMotivo(self, motivo):
        self.__motivo = motivo
    def setGravedad(self, gravedad):
        self.__gravedad = gravedad
    def setFechaIngreso(self, fechaIngreso):
        self.__feechaIngreso = fechaIngreso
    def setAtendido(self, atendido):
        self.__atendido = atendido

    # Metodo para representar el objeto como una cadena de texto.
    def __str__(self):
        return f"Paciente(idPaciente={self.__idPaciente}, nombre={self.__nombre}, edad={self.__edad}, genero={self.__genero}, motivo={self.__motivo}, gravedad={self.__gravedad}, fechaIngreso={self.__feechaIngreso}, atendido={self.__atendido})"