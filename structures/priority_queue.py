class Paciente:
    def __init__(self, id, nombre, edad, gravedad):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.gravedad = gravedad

class NodoCola:
    def __init__(self, paciente):
        self.paciente = paciente
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.frente = None

    def insertar(self, paciente):
        nuevo = NodoCola(paciente)
        if not self.frente or paciente.gravedad > self.frente.paciente.gravedad:
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            actual = self.frente
            while actual.siguiente and actual.siguiente.paciente.gravedad >= paciente.gravedad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def obtener_todos(self):
        result = []
        curr = self.frente
        while curr:
            result.append(curr.paciente)
            curr = curr.siguiente
        return result