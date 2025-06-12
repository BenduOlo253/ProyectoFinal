# Importa la clase Paciente desde el módulo structures.priority_queue
from structures.priority_queue import Paciente

# Función que guarda una lista de objetos Paciente en un archivo de texto
def guardar_pacientes(pacientes_lista):
    # Abre (o crea) el archivo en modo escritura
    with open("data/pacientes.txt", "w") as f:
        for p in pacientes_lista:
            # Escribe cada paciente como una línea en el archivo, separando los campos por comas
            f.write(f"{p.id},{p.nombre},{p.edad},{p.gravedad}\n")

# Función que carga los pacientes desde un archivo y los convierte en objetos Paciente
def cargar_pacientes():
    pacientes = []  # Lista que contendrá los objetos Paciente
    try:
        # Intenta abrir el archivo en modo lectura
        with open("data/pacientes.txt", "r") as f:
            for linea in f:
                # Divide la línea en los campos esperados
                id, nombre, edad, gravedad = linea.strip().split(",")
                # Crea un objeto Paciente y lo agrega a la lista (conversión de edad y gravedad a enteros)
                pacientes.append(Paciente(id, nombre, int(edad), int(gravedad)))
    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío
        open("data/pacientes.txt", "w").close()
    # Devuelve la lista de pacientes
    return pacientes