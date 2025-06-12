import tkinter as tk
from tkinter import messagebox

def abrir_ventana_principal(usuario):
    # Colores
    azul = "#1f77b4"
    blanco = "#e1e1e1"
    gris_oscuro = "#727272"

    def pass_func():
        pass

    principal = tk.Tk()
    principal.title("Sistema Hospitalario")
    principal.geometry("400x450")
    principal.configure(bg=gris_oscuro)

    frame_principal = tk.Frame(principal, bg=blanco, bd=3, relief="groove")
    frame_principal.pack(padx=10, pady=15, fill='both', expand=True) 
    
    label_bienvenida = tk.Label(
        frame_principal,
        text=f"Bienvenido, {usuario}",
        font=("Helvetica", 16, "bold"),
        bg=blanco,
        fg=azul
    )
    label_bienvenida.pack(pady=(10, 10))

    # Botones dentro del frame
    btn_config = {
        "master": frame_principal,  # ← corregido aquí
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
        "command": pass_func
    }

    # Crear botones
    tk.Button(**btn_config, text="Registrar Paciente").pack(pady=5)
    tk.Button(**btn_config, text="Ver Pacientes por Gravedad").pack(pady=5)
    tk.Button(**btn_config, text="Historial de Pacientes").pack(pady=5)
    tk.Button(**btn_config, text="Ver Historial de Accesos").pack(pady=5)
    tk.Button(**btn_config, text="Exportar Pacientes Ordenados").pack(pady=5)
    tk.Button(**btn_config, text="Cerrar Sesión").pack(pady=10)

    principal.mainloop()


abrir_ventana_principal("Usuario")
