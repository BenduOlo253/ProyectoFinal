class HistorialNodo:
    def __init__(self, usuario, accion, timestamp):
        self.usuario = usuario
        self.accion = accion
        self.timestamp = timestamp
        self.siguiente = None

class ListaHistorial:
    def __init__(self):
        self.cabeza = None

    def agregar(self, usuario, accion, timestamp):
        nuevo = HistorialNodo(usuario, accion, timestamp)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def obtener_historial(self):
        result = []
        curr = self.cabeza
        while curr:
            result.append((curr.usuario, curr.accion, curr.timestamp))
            curr = curr.siguiente
        return result