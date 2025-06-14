import tkinter as tk
from tkinter import messagebox

def abrir_ventana_principal(usuario):
    azul = "#1f77b4"
    blanco = "#ffffff"
    gris_oscuro = "#727272"

    def pass_func():
        pass

    principal = tk.Tk()
    principal.title("Sistema Hospitalario")
    principal.geometry("400x450")
    principal.configure(bg=gris_oscuro)

    frame_principal = tk.Frame(principal, bg=blanco, bd=3, relief="groove")
    frame_principal.pack(padx=10, pady=15, fill='both') 
    
    label_bienvenida = tk.Label(
        frame_principal,
        text=f"Bienvenido, {usuario}",
        font=("Helvetica", 16, "bold"),
        bg=blanco,
        fg=azul
    )
    label_bienvenida.pack(pady=(10, 10))

    # Botones 
    boton1 = tk.Button(
        frame_principal,
        text="Registrar Paciente",
        font=("Helvetica", 13),
        bg=azul,
        fg=blanco,
        activebackground="#145a86",
        activeforeground=blanco,
        bd=1,
        relief="groove",
        width=25,
        cursor="hand2",
        padx=10,
        pady=8,
        command=pass_func
    )
    boton1.pack(pady=5)

    boton2 = tk.Button(
        frame_principal,
        text="Ver Pacientes por Gravedad",
        font=("Helvetica", 13),
        bg=azul,
        fg=blanco,
        activebackground="#145a86",
        activeforeground=blanco,
        bd=1,
        relief="groove",
        width=25,
        cursor="hand2",
        padx=10,
        pady=8,
        command=pass_func
    )
    boton2.pack(pady=5)

    boton3 = tk.Button(
        frame_principal,
        text="Historial de Pacientes",
        font=("Helvetica", 13),
        bg=azul,
        fg=blanco,
        activebackground="#145a86",
        activeforeground=blanco,
        bd=1,
        relief="groove",
        width=25,
        cursor="hand2",
        padx=10,
        pady=8,
        command=pass_func
    )
    boton3.pack(pady=5)

    boton4 = tk.Button(
        frame_principal,
        text="Ver Historial de Accesos",
        font=("Helvetica", 13),
        bg=azul,
        fg=blanco,
        activebackground="#145a86",
        activeforeground=blanco,
        bd=1,
        relief="groove",
        width=25,
        cursor="hand2",
        padx=10,
        pady=8,
        command=pass_func
    )
    boton4.pack(pady=5)

    boton5 = tk.Button(
        frame_principal,
        text="Exportar Pacientes Ordenados",
        font=("Helvetica", 13),
        bg=azul,
        fg=blanco,
        activebackground="#145a86",
        activeforeground=blanco,
        bd=1,
        relief="groove",
        width=25,
        cursor="hand2",
        padx=10,
        pady=8,
        command=pass_func
    )
    boton5.pack(pady=5)

    boton6 = tk.Button(
        frame_principal,
        text="Cerrar Sesión",
        font=("Helvetica", 13),
        bg=azul,
        fg=blanco,
        activebackground="#145a86",
        activeforeground=blanco,
        bd=1,
        relief="groove",
        width=25,
        cursor="hand2",
        padx=10,
        pady=8,
        command=principal.destroy
    )
    boton6.pack(pady=10)

    principal.mainloop()

abrir_ventana_principal("Usuario")
