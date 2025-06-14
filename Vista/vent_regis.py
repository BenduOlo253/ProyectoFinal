import tkinter as tk


class VentanaRegistroPaciente:
    def __init__(self, ventana):
        # Crear ventana principal
        self.ventana = ventana
        ventana.title("Registro de Paciente - Sistema Hospitalario")
        ventana.geometry("450x520")
        ventana.configure(bg="#e1e1e1")  # fondo gris claro

        # Colores
        color_azul = "#1f77b4"
        color_blanco = "#ededed"

        # Título
        titulo = tk.Label(ventana, text="Registro de Paciente", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg=color_azul)
        titulo.pack(pady=20)

        # Marco de formulario
        frame = tk.Frame(ventana, bg=color_blanco, bd=2, relief="groove")
        frame.pack(padx=30, pady=10)

        # Lista de campos
        campos = [
            ("ID Paciente:", "id"),
            ("Nombre:", "nombre"),
            ("Edad:", "edad"),
            ("Género:", "genero"),
            ("Motivo:", "motivo"),
            ("Gravedad:", "gravedad"),
            ("Fecha Ingreso:", "fecha"),
            ("Atendido (Sí/No):", "atendido")
        ]

        # Diccionario para guardar referencias a las entradas
        entries = {}

        # Crear campos
        for i, (label_text, key) in enumerate(campos):
            label = tk.Label(frame, text=label_text, bg=color_blanco)
            label.grid(row=i, column=0, padx=10, pady=8, sticky="e")
            entry = tk.Entry(frame, width=25)
            entry.grid(row=i, column=1, padx=10, pady=8)
            entries[key] = entry

        # Botón de acción (sin funcionalidad asignada aún)
        boton_registro = tk.Button(ventana, text="Registrar Paciente", bg=color_azul, fg=color_blanco, width=20)
        boton_registro.pack(pady=20)
    
    def mostrar(self):
        self.ventana.mainloop()
    
    def registrarPaciente(self, ):
        from Controlador.ventPrincipalControlador import VentPrincipalControlador
        VentPrincipalControlador.registrarPaciente()
        self.ventana.destroy