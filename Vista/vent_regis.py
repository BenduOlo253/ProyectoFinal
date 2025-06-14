import tkinter as tk
from tkinter import messagebox

class VentanaRegistroPaciente:
    def __init__(self, ventana, controlador):
        self.ventana = ventana
        self.controlador = controlador

        ventana.title("Registro de Paciente - Sistema Hospitalario")
        ventana.geometry("450x520")
        ventana.configure(bg="#e1e1e1")  # fondo gris claro

        # Colores
        self.color_azul = "#1f77b4"
        self.color_blanco = "#ededed"

        # Título
        self.titulo = tk.Label(ventana, text="Registro de Paciente", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg=self.color_azul)
        self.titulo.pack(pady=20)

        # Marco de formulario
        self.frame = tk.Frame(ventana, bg=self.color_blanco, bd=2, relief="groove")
        self.frame.pack(padx=30, pady=10)

        # Campos y entradas guardados como listas paralelas
        self.labels_textos = [
            "ID Paciente:",
            "Nombre:",
            "Edad:",
            "Género:",
            "Motivo:",
            "Gravedad:",
            "Fecha Ingreso:",
            "Atendido (Sí/No):"
        ]

        self.entries = []  # lista para guardar las referencias a los Entry widgets

        for i, texto in enumerate(self.labels_textos):
            label = tk.Label(self.frame, text=texto, bg=self.color_blanco)
            label.grid(row=i, column=0, padx=10, pady=8, sticky="e")
            entry = tk.Entry(self.frame, width=25)
            entry.grid(row=i, column=1, padx=10, pady=8)
            self.entries.append(entry)

        # Botones
        self.boton_registro = tk.Button(ventana, text="Registrar Paciente", bg=self.color_azul, fg="white", width=20, command=self.registrarPaciente)
        self.boton_registro.pack(pady=15)

        self.boton_cancelar = tk.Button(ventana, text="Cancelar", bg="red", fg="white", width=20, command=self.cancelar)
        self.boton_cancelar.pack()

    def registrarPaciente(self):
        idPaciente = self.entries[0].get().strip()
        nombre = self.entries[1].get().strip()
        edad = self.entries[2].get().strip()
        genero = self.entries[3].get().strip()
        motivo = self.entries[4].get().strip()
        gravedad = self.entries[5].get().strip()
        fechaIngreso = self.entries[6].get().strip()
        atendido = self.entries[7].get().strip()

        if not idPaciente or not nombre or not edad or not genero or not motivo or not gravedad or not fechaIngreso:
            messagebox.showerror("Error", "Todos los campos excepto 'Atendido' son obligatorios.")
            return

        mensaje = self.controlador.registrarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechaIngreso, atendido)
        messagebox.showinfo("Registro", mensaje)

    def cancelar(self):
        self.ventana.destroy()
        # Abrir ventana login
        from Vista.vent_login import Login
        root_login = tk.Tk()
        Login(root_login).mostrar()

    def mostrar(self):
        self.ventana.mainloop()
