class TablaHashDoble:
    def __init__(self, tamaño=50):
        self.tamaño = tamaño
        self.tabla = [None] * tamaño
        self.valores = [None] * tamaño  # para claves

    def _hash1(self, clave):
        return sum(ord(c) for c in clave) % self.tamaño

    def _hash2(self, clave):
        # Segunda función hash, evita múltiplos de tamaño
        return 1 + (sum(ord(c) for c in clave) % (self.tamaño - 1))

    def _sonIguales(self, a, b):
        return a == b

    def insertarValor(self, clave, valor):
        idx = self._hash1(clave)
        salto = self._hash2(clave)

        for i in range(self.tamaño):
            nuevo_idx = (idx + i * salto) % self.tamaño
            if self.tabla[nuevo_idx] is None or self.valores[nuevo_idx] == clave:
                self.tabla[nuevo_idx] = valor
                self.valores[nuevo_idx] = clave
                return
        raise Exception("Tabla Hash llena")

    def obtenerValor(self, clave):
        idx = self._hash1(clave)
        salto = self._hash2(clave)

        for i in range(self.tamaño):
            nuevo_idx = (idx + i * salto) % self.tamaño
            if self.valores[nuevo_idx] == clave:
                return self.tabla[nuevo_idx]
            if self.tabla[nuevo_idx] is None:
                break
        return None

    def eliminarValor(self, clave):
        idx = self._hash1(clave)
        salto = self._hash2(clave)

        for i in range(self.tamaño):
            nuevo_idx = (idx + i * salto) % self.tamaño
            if self.valores[nuevo_idx] == clave:
                self.tabla[nuevo_idx] = None
                self.valores[nuevo_idx] = None
                return True
            if self.tabla[nuevo_idx] is None:
                break
        return False
