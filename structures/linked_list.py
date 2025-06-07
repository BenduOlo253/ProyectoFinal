# Clase que representa un nodo del historial de acciones
class HistorialNodo:
    def __init__(self, usuario, accion, timestamp):
        self.usuario = usuario          # Nombre o identificador del usuario
        self.accion = accion            # Descripción de la acción realizada
        self.timestamp = timestamp      # Marca de tiempo en que ocurrió la acción
        self.siguiente = None           # Referencia al siguiente nodo en la lista

# Clase que representa una lista enlazada simple para almacenar historial de acciones
class ListaHistorial:
    def __init__(self):
        self.cabeza = None              # Referencia al primer nodo de la lista

    # Agrega una nueva entrada al historial (al inicio de la lista)
    def agregar(self, usuario, accion, timestamp):
        nuevo = HistorialNodo(usuario, accion, timestamp)  # Crear un nuevo nodo con los datos
        nuevo.siguiente = self.cabeza                      # Apuntar el nuevo nodo al nodo actual
        self.cabeza = nuevo                                # Actualizar la cabeza al nuevo nodo

    # Retorna una lista con todas las entradas del historial como tuplas
    def obtener_historial(self):
        result = []                        # Lista para almacenar las entradas
        curr = self.cabeza                # Empezar desde la cabeza de la lista

        while curr:
            # Agregar los datos del nodo actual a la lista de resultados
            result.append((curr.usuario, curr.accion, curr.timestamp))
            curr = curr.siguiente         # Avanzar al siguiente nodo

        return result                      # Devolver la lista de entradas
