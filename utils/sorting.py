# Función de ordenamiento Merge Sort para una lista de pacientes
# Se ordena según el atributo especificado en 'clave' (por ejemplo: 'edad', 'gravedad', etc.)
def merge_sort(pacientes, clave):
    # Caso base: una lista con 0 o 1 elementos ya está ordenada
    if len(pacientes) <= 1:
        return pacientes

    # Dividir la lista a la mitad
    medio = len(pacientes) // 2
    izq = merge_sort(pacientes[:medio], clave)   # Ordenar la mitad izquierda
    der = merge_sort(pacientes[medio:], clave)   # Ordenar la mitad derecha

    # Combinar ambas mitades ordenadas
    return merge(izq, der, clave)

# Función auxiliar que combina dos listas ordenadas en una sola
def merge(izq, der, clave):
    resultado = []  # Lista resultante ordenada
    i = j = 0       # Índices para recorrer ambas mitades

    # Combinar elementos de las listas izq y der comparando por el atributo 'clave'
    while i < len(izq) and j < len(der):
        if getattr(izq[i], clave) <= getattr(der[j], clave):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # Añadir cualquier elemento restante (ya ordenado) de ambas mitades
    resultado.extend(izq[i:])
    resultado.extend(der[j:])

    return resultado  # Devolver la lista ordenada final
