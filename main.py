import tkinter as tk
from tkinter import messagebox, simpledialog
from structures.hash_table import HashTable
from structures.priority_queue import ColaPrioridad, Paciente
from structures.linked_list import ListaHistorial
from utils.timestamp import current_timestamp
from utils.paciente_io import guardar_pacientes, cargar_pacientes
from utils.sorting import merge_sort
from utils.access_log import leer_historial_accesos

# Cargar usuarios en hash table
users = HashTable()
USERS_FILE = "data/users.txt"
ACCESS_LOG_FILE = "data/access_log.txt"
PACIENTES_FILE = "data/pacientes.txt"

# Cargar usuarios desde archivo
def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            for line in f:
                u, p = line.strip().split(",")
                users.insert(u, p)
    except FileNotFoundError:
        open(USERS_FILE, "w").close()

# Registrar nuevo usuario
def register_user(username, password):
    if users.search(username):
        return False, "Usuario ya existe."
    users.insert(username, password)
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")
    return True, "Usuario registrado correctamente."

# Verificar login
def login_user(username, password):
    stored = users.search(username)
    if stored and stored == password:
        log_access(username, "entrada")
        return True
    return False

# Registrar acceso
def log_access(username, action):
    with open(ACCESS_LOG_FILE, "a") as f:
        f.write(f"{username},{action},{current_timestamp()}\n")

# Ventana principal
def abrir_ventana_principal(usuario):
    principal = tk.Tk()
    principal.title("Sistema Hospitalario")
    principal.geometry("600x400")

    # Estructuras
    pacientes_queue = ColaPrioridad()
    historial = ListaHistorial()

    # Cargar pacientes persistentes
    for p in cargar_pacientes():
        pacientes_queue.insertar(p)

    def registrar_paciente():
        id_p = simpledialog.askstring("ID", "ID del paciente:", parent=principal)
        if id_p is None:
            return
        nombre = simpledialog.askstring("Nombre", "Nombre del paciente:", parent=principal)
        if nombre is None:
            return
        edad = simpledialog.askinteger("Edad", "Edad del paciente:", parent=principal, minvalue=0)
        if edad is None:
            return
        gravedad = simpledialog.askinteger("Gravedad (1-10)", "Nivel de gravedad:", parent=principal, minvalue=1, maxvalue=10)
        if gravedad is None:
            return

        paciente = Paciente(id_p, nombre, edad, gravedad)
        pacientes_queue.insertar(paciente)
        accion = f"Registró paciente {nombre} con gravedad {gravedad}"
        historial.agregar(usuario, accion, current_timestamp())
        messagebox.showinfo("Paciente registrado", f"Paciente {nombre} añadido con éxito.", parent=principal)

    def ver_pacientes():
        lista = pacientes_queue.obtener_todos()
        if not lista:
            messagebox.showinfo("Pacientes", "No hay pacientes registrados.", parent=principal)
            return
        salida = "\n".join([f"ID: {p.id} | Nombre: {p.nombre} | Edad: {p.edad} | Gravedad: {p.gravedad}" for p in lista])
        messagebox.showinfo("Pacientes por Gravedad", salida, parent=principal)

    def ver_historial_pacientes():
        registros = historial.obtener_historial()
        if not registros:
            messagebox.showinfo("Historial Pacientes", "No hay historial de pacientes.", parent=principal)
            return
        salida = "\n".join([f"{u} hizo '{a}' a las {t}" for u, a, t in registros])
        messagebox.showinfo("Historial de Actividad de Pacientes", salida, parent=principal)

    def ver_historial_accesos_gui():
        accesos = leer_historial_accesos()
        if not accesos:
            messagebox.showinfo("Historial de Accesos", "No hay registros de accesos.", parent=principal)
            return
        salida = "\n".join([f"{u} - {a} - {t}" for u, a, t in accesos])
        messagebox.showinfo("Historial de Accesos", salida, parent=principal)

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

    def cerrar_sesion():
        guardar_pacientes(pacientes_queue.obtener_todos())
        log_access(usuario, "salida")
        principal.destroy()

    # Widgets
    tk.Label(principal, text=f"Bienvenido, {usuario}", font=("Arial", 16)).pack(pady=10)

    btn_registrar = tk.Button(principal, text="Registrar Paciente", command=registrar_paciente)
    btn_registrar.pack(pady=5)

    btn_ver = tk.Button(principal, text="Ver Pacientes por Gravedad", command=ver_pacientes)
    btn_ver.pack(pady=5)

    btn_hist_pac = tk.Button(principal, text="Historial de Pacientes", command=ver_historial_pacientes)
    btn_hist_pac.pack(pady=5)

    btn_hist_acc = tk.Button(principal, text="Ver Historial de Accesos", command=ver_historial_accesos_gui)
    btn_hist_acc.pack(pady=5)

    btn_ord = tk.Button(principal, text="Exportar Pacientes Ordenados", command=exportar_ordenados)
    btn_ord.pack(pady=5)

    btn_cerrar = tk.Button(principal, text="Cerrar Sesión", command=cerrar_sesion)
    btn_cerrar.pack(pady=20)

    principal.mainloop()

# Interfaz de Login y Registro
def mostrar_login():
    login_win = tk.Tk()
    login_win.title("Login - Sistema Hospitalario")
    login_win.geometry("300x220")

    tk.Label(login_win, text="Usuario").pack(pady=5)
    entry_user = tk.Entry(login_win)
    entry_user.pack()

    tk.Label(login_win, text="Contraseña").pack(pady=5)
    entry_pass = tk.Entry(login_win, show="*")
    entry_pass.pack()

    def attempt_login():
        u = entry_user.get().strip()
        p = entry_pass.get().strip()
        if login_user(u, p):
            messagebox.showinfo("Login", "Acceso exitoso", parent=login_win)
            login_win.destroy()
            abrir_ventana_principal(u)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas", parent=login_win)

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

    tk.Button(login_win, text="Iniciar Sesión", command=attempt_login).pack(pady=10)
    tk.Button(login_win, text="Registrarse", command=mostrar_registro).pack()
    login_win.mainloop()

if __name__ == "__main__":
    load_users()
    # Asegurar existencia de archivos
    open(ACCESS_LOG_FILE, "a").close()
    open(PACIENTES_FILE, "a").close()
    mostrar_login()