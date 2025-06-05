def merge_sort(pacientes, clave):
    if len(pacientes) <= 1:
        return pacientes
    medio = len(pacientes) // 2
    izq = merge_sort(pacientes[:medio], clave)
    der = merge_sort(pacientes[medio:], clave)
    return merge(izq, der, clave)

def merge(izq, der, clave):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if getattr(izq[i], clave) <= getattr(der[j], clave):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado