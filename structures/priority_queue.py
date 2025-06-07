# Clase que representa a un paciente con atributos básicos
class Paciente:
    def __init__(self, id, nombre, edad, gravedad):
        self.id = id                # Identificador único del paciente
        self.nombre = nombre        # Nombre del paciente
        self.edad = edad            # Edad del paciente
        self.gravedad = gravedad    # Nivel de gravedad (prioridad): entre más alto, más urgente

# Nodo que almacena un paciente y apunta al siguiente nodo en la cola
class NodoCola:
    def __init__(self, paciente):
        self.paciente = paciente        # Objeto Paciente
        self.siguiente = None           # Referencia al siguiente nodo

# Cola de prioridad implementada como lista enlazada
class ColaPrioridad:
    def __init__(self):
        self.frente = None              # Inicio de la cola (paciente con mayor prioridad)

    # Inserta un paciente en la cola respetando el orden de prioridad (gravedad descendente)
    def insertar(self, paciente):
        nuevo = NodoCola(paciente)  # Crear un nodo con el paciente
        # Si la cola está vacía o el nuevo paciente tiene mayor gravedad que el primero
        if not self.frente or paciente.gravedad > self.frente.paciente.gravedad:
            nuevo.siguiente = self.frente   # Insertar al inicio
            self.frente = nuevo
        else:
            actual = self.frente
            # Buscar la posición correcta según la gravedad
            while actual.siguiente and actual.siguiente.paciente.gravedad >= paciente.gravedad:
                actual = actual.siguiente
            # Insertar el nuevo nodo en la posición encontrada
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    # Devuelve una lista con todos los pacientes en orden de prioridad
    def obtener_todos(self):
        result = []
        curr = self.frente
        while curr:
            result.append(curr.paciente)  # Agregar el paciente actual a la lista
            curr = curr.siguiente         # Avanzar al siguiente nodo
        return result
