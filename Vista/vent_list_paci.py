import tkinter as tk
from tkinter import ttk
from Controlador.listaPacientesControlador import ListaPacientesControlador

class VentanaListaPacientes:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de Pacientes Registrados")
        self.ventana.geometry("800x400")
        self.ventana.configure(bg="#e1e1e1")

        self.color_azul = "#1f77b4"
        self.color_blanco = "#ffffff"

        self.titulo = tk.Label(
            self.ventana,
            text="Pacientes Registrados",
            font=("Helvetica", 16, "bold"),
            bg="#f0f0f0",
            fg=self.color_azul
        )
        self.titulo.pack(pady=20)

        self.frame_tabla = tk.Frame(self.ventana, bg=self.color_blanco, bd=2, relief="groove")
        self.frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

        self.columnas = ["id", "nombre", "edad", "genero", "motivo", "gravedad", "fechaIngreso", "atendido"]

        self.tabla = ttk.Treeview(self.frame_tabla, columns=self.columnas, show="headings")

        encabezados = [
            "ID Paciente", "Nombre", "Edad", "Género",
            "Motivo", "Gravedad", "Fecha Ingreso", "Atendido"
        ]

        for i in range(len(self.columnas)):
            self.tabla.heading(self.columnas[i], text=encabezados[i])
            self.tabla.column(self.columnas[i], width=100, anchor="center")

        self.scrollbar_y = ttk.Scrollbar(self.frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_y.pack(side="right", fill="y")

        self.tabla.pack(fill="both", expand=True)

        self.cargar_pacientes()

    def cargar_pacientes(self):
        pacientes = ListaPacientesControlador.obtenerPacientesListaSimple()

        # Limpiar tabla antes de insertar
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Insertar filas
        for paciente in pacientes:
            self.tabla.insert("", "end", values=paciente)

    def mostrar(self):
        self.ventana.mainloop()
