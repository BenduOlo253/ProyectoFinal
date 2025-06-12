# Importación de módulos necesarios
#joula
import tkinter as tk
from tkinter import messagebox, simpledialog
from structures.hash_table import HashTable
from structures.priority_queue import ColaPrioridad, Paciente
from structures.linked_list import ListaHistorial
from utils.timestamp import current_timestamp
from utils.paciente_io import guardar_pacientes, cargar_pacientes
from utils.sorting import merge_sort
from utils.access_log import leer_historial_accesos
#registro#
# Constantes para rutas de archivos
USERS_FILE = "data/users.txt"
ACCESS_LOG_FILE = "data/access_log.txt"
PACIENTES_FILE = "data/pacientes.txt"

# Estructura hash para almacenar usuarios (username -> password)
users = HashTable()

# Carga los usuarios existentes desde el archivo
def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                users.insert(u, p)
    except FileNotFoundError:
        open(USERS_FILE, "w").close()  # Crea el archivo si no existe

# Registra un nuevo usuario en la hash table y en el archivo
def register_user(username, password):
    if users.search(username):
        return False, "Usuario ya existe."
    users.insert(username, password)
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")
    return True, "Usuario registrado correctamente."

# Verifica las credenciales del usuario
def login_user(username, password):
    stored = users.search(username)
    if stored and stored == password:
        log_access(username, "entrada")
        return True
    return False

# Registra una acción de acceso al sistema con timestamp
def log_access(username, action):
    with open(ACCESS_LOG_FILE, "a") as f:
        f.write(f"{username},{action},{current_timestamp()}\n")

# Ventana principal que se abre después del login exitoso
def abrir_ventana_principal(usuario):
    principal = tk.Tk()
    principal.title("Sistema Hospitalario")
    principal.geometry("400x450")
    principal.configure(bg=gris_oscuro)

    #colores
    azul="#1f77b4"
    blanco = "#ffffff"
    gris = "#e1e1e1"
    gris_oscuro= "#d7d7d7"
    # Estructuras internas
    pacientes_queue = ColaPrioridad()
    historial = ListaHistorial()

    # Carga los pacientes previamente registrados
    for p in cargar_pacientes():
        pacientes_queue.insertar(p)

    # Función para registrar un nuevo paciente
    def registrar_paciente():
        id_p = simpledialog.askstring("ID", "ID del paciente:", parent=principal)
        if id_p is None: return
        nombre = simpledialog.askstring("Nombre", "Nombre del paciente:", parent=principal)
        if nombre is None: return
        edad = simpledialog.askinteger("Edad", "Edad del paciente:", parent=principal, minvalue=0)
        if edad is None: return
        gravedad = simpledialog.askinteger("Gravedad (1-10)", "Nivel de gravedad:", parent=principal, minvalue=1, maxvalue=10)
        if gravedad is None: return

        paciente = Paciente(id_p, nombre, edad, gravedad)
        pacientes_queue.insertar(paciente)
        historial.agregar(usuario, f"Registró paciente {nombre} con gravedad {gravedad}", current_timestamp())
        messagebox.showinfo("Paciente registrado", f"Paciente {nombre} añadido con éxito.", parent=principal)

    # Muestra los pacientes ordenados por prioridad (gravedad)
    def ver_pacientes():
        lista = pacientes_queue.obtener_todos()
        if not lista:
            messagebox.showinfo("Pacientes", "No hay pacientes registrados.", parent=principal)
            return
        salida = "\n".join([f"ID: {p.id} | Nombre: {p.nombre} | Edad: {p.edad} | Gravedad: {p.gravedad}" for p in lista])
        messagebox.showinfo("Pacientes por Gravedad", salida, parent=principal)

    # Muestra el historial de acciones realizadas por el usuario actual
    def ver_historial_pacientes():
        registros = historial.obtener_historial()
        if not registros:
            messagebox.showinfo("Historial Pacientes", "No hay historial de pacientes.", parent=principal)
            return
        salida = "\n".join([f"{u} hizo '{a}' a las {t}" for u, a, t in registros])
        messagebox.showinfo("Historial de Actividad de Pacientes", salida, parent=principal)

    # Muestra el historial de accesos al sistema
    def ver_historial_accesos_gui():
        accesos = leer_historial_accesos()
        if not accesos:
            messagebox.showinfo("Historial de Accesos", "No hay registros de accesos.", parent=principal)
            return
        salida = "\n".join([f"{u} - {a} - {t}" for u, a, t in accesos])
        messagebox.showinfo("Historial de Accesos", salida, parent=principal)

    # Ordena pacientes por nombre o edad y los muestra
    def exportar_ordenados():
        criterio = simpledialog.askstring("Ordenar por", "¿Ordenar por 'nombre' o 'edad'?", parent=principal)
        if criterio not in ["nombre", "edad"]:
            messagebox.showerror("Error", "Criterio inválido.", parent=principal)
            return
        lista = pacientes_queue.obtener_todos()
        if not lista:
            messagebox.showinfo("Pacientes Ordenados", "No hay pacientes.", parent=principal)
            return
        ordenados = merge_sort(lista, criterio)
        salida = "\n".join([f"ID: {p.id} | Nombre: {p.nombre} | Edad: {p.edad} | Gravedad: {p.gravedad}" for p in ordenados])
        messagebox.showinfo("Pacientes Ordenados", salida, parent=principal)

    # Guarda pacientes y cierra la sesión
    def cerrar_sesion():
        guardar_pacientes(pacientes_queue.obtener_todos())
        log_access(usuario, "salida")
        principal.destroy()


    # Marco principal para contener todo el contenido
    frame_principal = tk.Frame(principal, bg=blanco, bd=3, relief="groove")
    frame_principal.pack(padx=10, pady=15, fill='both') 
    
    label_bienvenida = tk.Label(frame_principal, text=f"Bienvenido, {usuario}", font=("Helvetica", 16, "bold"), bg=blanco, fg=azul)
    label_bienvenida.pack(pady=(10, 10))

    # Widgets de la ventana principal

# Botones con estilo y padding
    btn_config = {
        "master": principal,
        "font": ("Helvetica", 13),
        "bg": azul,
        "fg": blanco,
        "activebackground": "#145a86",
        "activeforeground": blanco,
        "bd": 1,
        "relief": "groove",
        "width": 25,
        "cursor": "hand2",
        "padx": 10,
        "pady": 8,
    }


    tk.Button(**btn_config, text="Registrar Paciente", command=registrar_paciente).pack(pady=5)
    tk.Button(**btn_config, text="Ver Pacientes por Gravedad", command=ver_pacientes).pack(pady=5)
    tk.Button(**btn_config, text="Historial de Pacientes", command=ver_historial_pacientes).pack(pady=5)
    tk.Button(**btn_config, text="Ver Historial de Accesos", command=ver_historial_accesos_gui).pack(pady=5)
    tk.Button(**btn_config, text="Exportar Pacientes Ordenados", command=exportar_ordenados).pack(pady=5)
    tk.Button(**btn_config, text="Cerrar Sesión", command=cerrar_sesion).pack(pady=10)

    principal.mainloop()

# Ventana de login inicial del sistema
def mostrar_login():
    login_win = tk.Tk()
    login_win.title("Login - Sistema Hospitalario")
    login_win.geometry("500x400")
    login_win.configure(bg="#f0f0f0")

    #colores
    azul="#1f77b4"
    blanco = "#ffffff"
    gris = "#e1e1e1"

    # Etiqueta de título
    titulo = tk.Label(login_win, text="Sistema Hospitalario", font=("Helvetica", 16, "bold"), bg="#ffffff", bd=0.5, relief="groove", fg=azul)
    titulo.pack(pady=20)

    # Frame para los campos, con fondo blanco y borde
    frame_campos = tk.Frame(login_win, bg=blanco, bd=2, relief="groove")
    frame_campos.pack(padx=20, pady=20)

    # Campo de usuario
    label_usuario = tk.Label(frame_campos, text="Nombre de usuario:", bg=blanco, fg="black", font=("Helvetica", 13))
    label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_user = tk.Entry(frame_campos, width=30, bd=3, relief="groove")
    entry_user.grid(row=0, column=1, padx=10, pady=10)

    # Campo de contraseña
    label_contrasena = tk.Label(frame_campos, text="Contraseña:", bg=blanco, fg="black", font=("Helvetica", 13))
    label_contrasena.grid(row=1, column=0, padx=10, pady=10, sticky="e")
    entry_pass = tk.Entry(frame_campos, show="*", width=30, bd=3, relief="groove")
    entry_pass.grid(row=1, column=1, padx=10, pady=10)


    # Intenta iniciar sesión con las credenciales dadas
    def attempt_login():
        u = entry_user.get().strip()
        p = entry_pass.get().strip()
        if login_user(u, p):
            messagebox.showinfo("Login", "Acceso exitoso", parent=login_win)
            login_win.destroy()
            abrir_ventana_principal(u)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas", parent=login_win)

    # Abre una subventana para registrar un nuevo usuario
    def mostrar_registro():
        reg_win = tk.Toplevel(login_win)
        reg_win.title("Registro - Sistema Hospitalario")
        reg_win.geometry("300x220")

        tk.Label(reg_win, text="Usuario").pack(pady=5)
        entry_user_r = tk.Entry(reg_win)
        entry_user_r.pack()

        tk.Label(reg_win, text="Contraseña").pack(pady=5)
        entry_pass_r = tk.Entry(reg_win, show="*")
        entry_pass_r.pack()

        # Intenta registrar un nuevo usuario
        def attempt_register():
            u = entry_user_r.get().strip()
            p = entry_pass_r.get().strip()
            if not u or not p:
                messagebox.showerror("Error", "Completa todos los campos", parent=reg_win)
                return
            success, msg = register_user(u, p)
            if success:
                messagebox.showinfo("Registro", msg, parent=reg_win)
                reg_win.destroy()
            else:
                messagebox.showerror("Error", msg, parent=reg_win)

        tk.Button(reg_win, text="Registrar", command=attempt_register).pack(pady=10)

    # Botones de login y registro
    tk.Button(login_win, text="Iniciar Sesión", command=attempt_login, bg=azul,fg=blanco, font=("Helvetica", 10, "bold"), activebackground=gris,
    activeforeground="black", bd=2, relief="groove", width=20).pack(pady=10)

    tk.Button(login_win, text="Registrarse", command=mostrar_registro, bg=gris, fg="black", font=("Helvetica", 10, "bold"), activebackground=azul, activeforeground=blanco, 
    bd=2, relief="groove", width=20).pack()
    
    login_win.mainloop()

# Punto de entrada del programa
if __name__ == "__main__":
    load_users()  # Carga usuarios desde archivo
    open(ACCESS_LOG_FILE, "a").close()  # Asegura que existan los archivos
    open(PACIENTES_FILE, "a").close()
    mostrar_login()  # Muestra la interfaz de login


 