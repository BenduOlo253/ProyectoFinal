from structures.listaEnlazada import ListaEnlazada

class TablaHash:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [ListaEnlazada() for _ in range(tamaño)]

    def _hash(self, clave):
        return sum(ord(c) for c in clave) % self.tamaño

    def insertarValor(self, clave, valor):
        indice = self._hash(clave)
        self.tabla[indice].insertar(clave, valor)

    def obtenerValor(self, clave):
        indice = self._hash(clave)
        return self.tabla[indice].buscar(clave)
    

    def eliminarValor(self, clave):
        indice = self._hash(clave)
        return self.tabla[indice].eliminar(clave)