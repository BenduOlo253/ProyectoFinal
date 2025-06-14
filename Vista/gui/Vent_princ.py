import tkinter as tk
from tkinter import messagebox

def abrir_ventana_principal(usuario):
    from Controlador.ventPrincipalControlador import PacienteService

    azul = "#1f77b4"
    blanco = "#ffffff"
    gris_oscuro = "#727272"

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

    def registrar_paciente():
        RegistroPacienteControlador.abrir_formulario_registro()

    def ver_pacientes_por_gravedad():
        VisualizacionControlador.mostrar_por_gravedad()

    def ver_historial_pacientes():
        HistorialControlador.mostrar_historial()

    def ver_historial_accesos():
        HistorialControlador.mostrar_accesos()

    def exportar_pacientes_ordenados():
        ExportacionControlador.exportar_ordenados()

    def cerrar_sesion():
        principal.destroy()

    # Botones
    tk.Button(
        frame_principal, text="Registrar Paciente", font=("Helvetica", 13),
        bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
        bd=1, relief="groove", width=25, cursor="hand2",
        padx=10, pady=8, command=registrar_paciente
    ).pack(pady=5)

    tk.Button(
        frame_principal, text="Ver Pacientes por Gravedad", font=("Helvetica", 13),
        bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
        bd=1, relief="groove", width=25, cursor="hand2",
        padx=10, pady=8, command=ver_pacientes_por_gravedad
    ).pack(pady=5)

    tk.Button(
        frame_principal, text="Historial de Pacientes", font=("Helvetica", 13),
        bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
        bd=1, relief="groove", width=25, cursor="hand2",
        padx=10, pady=8, command=ver_historial_pacientes
    ).pack(pady=5)

    tk.Button(
        frame_principal, text="Ver Historial de Accesos", font=("Helvetica", 13),
        bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
        bd=1, relief="groove", width=25, cursor="hand2",
        padx=10, pady=8, command=ver_historial_accesos
    ).pack(pady=5)

    tk.Button(
        frame_principal, text="Exportar Pacientes Ordenados", font=("Helvetica", 13),
        bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
        bd=1, relief="groove", width=25, cursor="hand2",
        padx=10, pady=8, command=exportar_pacientes_ordenados
    ).pack(pady=5)

    tk.Button(
        frame_principal, text="Cerrar Sesión", font=("Helvetica", 13),
        bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
        bd=1, relief="groove", width=25, cursor="hand2",
        padx=10, pady=8, command=cerrar_sesion
    ).pack(pady=10)

    principal.mainloop()
