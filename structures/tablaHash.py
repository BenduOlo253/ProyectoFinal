from structures.listaEnlazada import ListaEnlazada

class TablaHash:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [ListaEnlazada() for _ in range(tamaño)]

    def _hash(self, clave):
        return sum(ord(c) for c in clave) % self.tamaño

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        self.tabla[indice].insertar(clave, valor)

    def obtener(self, clave):
        indice = self._hash(clave)
        return self.tabla[indice].buscar(clave)

    def eliminar(self, clave):
        indice = self._hash(clave)
        return self.tabla[indice].eliminar(clave)

    def mostrar(self):
        for i, lista in enumerate(self.tabla):
            print(f"Índice {i}: ", end="")
            for nodo in lista:
                print(f"({nodo.clave}: {nodo.valor})", end=" -> ")
            print("None")
