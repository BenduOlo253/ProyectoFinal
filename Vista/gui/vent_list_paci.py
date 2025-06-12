import tkinter as tk
from tkinter import ttk

# Crear ventana de visualización
ventana = tk.Tk()
ventana.title("Lista de Pacientes Registrados")
ventana.geometry("800x400")
ventana.configure(bg="#e1e1e1")

# Colores
color_azul = "#1f77b4"
color_blanco = "#ffffff"

# Título
titulo = tk.Label(ventana, text="Pacientes Registrados", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg=color_azul)
titulo.pack(pady=20)

# Marco de la tabla
frame_tabla = tk.Frame(ventana, bg=color_blanco, bd=2, relief="groove")
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

# Definir columnas
columnas = ("id", "nombre", "edad", "genero", "motivo", "gravedad", "fechaIngreso", "atendido")

# Crear Treeview
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

# Definir encabezados
tabla.heading("id", text="ID Paciente")
tabla.heading("nombre", text="Nombre")
tabla.heading("edad", text="Edad")
tabla.heading("genero", text="Género")
tabla.heading("motivo", text="Motivo")
tabla.heading("gravedad", text="Gravedad")
tabla.heading("fechaIngreso", text="Fecha Ingreso")
tabla.heading("atendido", text="Atendido")

# Ajustar el ancho de las columnas
for col in columnas:
    tabla.column(col, width=100, anchor="center")

# Agregar scrollbar
scrollbar_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.pack(side="right", fill="y")

tabla.pack(fill="both", expand=True)

# Ejecutar ventana
ventana.mainloop()
