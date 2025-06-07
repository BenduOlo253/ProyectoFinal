# Clase que representa un nodo de la tabla hash (usado para manejar colisiones con encadenamiento)
class HashNode:
    def __init__(self, key, value):
        self.key = key      # Clave del nodo
        self.value = value  # Valor asociado a la clave
        self.next = None    # Puntero al siguiente nodo en caso de colisión (encadenamiento)

# Clase que representa la tabla hash
class HashTable:
    def __init__(self, size=100):
        self.size = size                   # Tamaño de la tabla
        self.table = [None] * size         # Arreglo que contiene las listas de nodos

    # Función hash simple: suma de los valores ASCII de los caracteres del string módulo el tamaño
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    # Inserta una clave y su valor en la tabla hash
    def insert(self, key, value):
        idx = self._hash(key)              # Calcula el índice usando la función hash
        new_node = HashNode(key, value)    # Crea un nuevo nodo con la clave y el valor

        if self.table[idx] is None:
            # Si no hay colisión, se inserta directamente
            self.table[idx] = new_node
        else:
            # Si hay colisión, se recorre la lista enlazada
            curr = self.table[idx]
            while True:
                if curr.key == key:
                    # Si la clave ya existe, se actualiza el valor
                    curr.value = value
                    return
                if curr.next is None:
                    break
                curr = curr.next
            # Se añade el nuevo nodo al final de la lista
            curr.next = new_node

    # Busca el valor asociado a una clave en la tabla hash
    def search(self, key):
        idx = self._hash(key)      # Calcula el índice usando la función hash
        curr = self.table[idx]     # Obtiene el nodo inicial en ese índice

        while curr:
            if curr.key == key:
                # Si se encuentra la clave, se devuelve el valor
                return curr.value
            curr = curr.next
        # Si no se encuentra la clave, se devuelve None
        return None
