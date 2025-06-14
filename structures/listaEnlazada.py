#Lista enlazada para almacenar pares clave-valor para la tabla hash.
class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, clave, valor):
        # Si ya existe, reemplaza
        nodo = self.cabeza
        while nodo:
            if nodo.clave == clave:
                nodo.valor = valor
                return
            nodo = nodo.siguiente
        nuevo = Nodo(clave, valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar(self, clave):
        nodo = self.cabeza
        while nodo:
            if nodo.clave == clave:
                return nodo.valor
            nodo = nodo.siguiente
        return None

    def eliminar(self, clave):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.clave == clave:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def __iter__(self):
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente
