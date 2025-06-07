# Función que lee el historial de accesos desde un archivo de texto
def leer_historial_accesos():
    historial = []  # Lista donde se almacenarán las entradas del historial

    try:
        # Intenta abrir el archivo de historial en modo lectura
        with open("data/access_log.txt", "r") as f:
            for linea in f:
                # Elimina espacios en blanco y divide la línea en usuario, acción y hora
                usuario, accion, hora = linea.strip().split(",")
                # Agrega la tupla a la lista del historial
                historial.append((usuario, accion, hora))

    except FileNotFoundError:
        # Si el archivo no existe, lo crea vacío para evitar errores futuros
        open("data/access_log.txt", "w").close()

    # Devuelve la lista con las entradas del historial
    return historial
