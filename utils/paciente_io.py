from structures.priority_queue import Paciente

def guardar_pacientes(pacientes_lista):
    with open("data/pacientes.txt", "w") as f:
        for p in pacientes_lista:
            f.write(f"{p.id},{p.nombre},{p.edad},{p.gravedad}\n")

def cargar_pacientes():
    pacientes = []
    try:
        with open("data/pacientes.txt", "r") as f:
            for linea in f:
                id, nombre, edad, gravedad = linea.strip().split(",")
                pacientes.append(Paciente(id, nombre, int(edad), int(gravedad)))
    except FileNotFoundError:
        open("data/pacientes.txt", "w").close()
    return pacientes