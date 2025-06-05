def leer_historial_accesos():
    historial = []
    try:
        with open("data/access_log.txt", "r") as f:
            for linea in f:
                usuario, accion, hora = linea.strip().split(",")
                historial.append((usuario, accion, hora))
    except FileNotFoundError:
        open("data/access_log.txt", "w").close()
    return historial