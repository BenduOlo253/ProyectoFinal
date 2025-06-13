# Importa la clase datetime para trabajar con fechas y horas actuales
from datetime import datetime

# Función que devuelve la fecha y hora actual como una cadena formateada
def current_timestamp():
    # Obtiene la fecha y hora actual y la formatea como 'YYYY-MM-DD HH:MM:SS'
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")