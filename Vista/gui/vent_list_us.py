import tkinter as tk
from tkinter import ttk

# Crear ventana de visualización
ventana = tk.Tk()
ventana.title("Lista de Usuarios Registrados")
ventana.geometry("600x350")
ventana.configure(bg="#e1e1e1")

# Colores
color_azul = "#1f77b4"
color_blanco = "#ffffff"

# Título
titulo = tk.Label(ventana, text="Usuarios Registrados", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg=color_azul)
titulo.pack(pady=20)

# Marco de la tabla
frame_tabla = tk.Frame(ventana, bg=color_blanco, bd=2, relief="groove")
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

# Definir columnas
columnas = ("idUsuario", "nombre", "contraseña", "rol")

# Crear Treeview
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

# Definir encabezados
tabla.heading("idUsuario", text="ID Usuario")
tabla.heading("nombre", text="Nombre")
tabla.heading("contraseña", text="Contraseña")
tabla.heading("rol", text="Rol")

# Ajustar ancho de columnas
tabla.column("idUsuario", width=100, anchor="center")
tabla.column("nombre", width=150, anchor="center")
tabla.column("contraseña", width=150, anchor="center")
tabla.column("rol", width=100, anchor="center")

# Scrollbar vertical
scrollbar_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.pack(side="right", fill="y")

tabla.pack(fill="both", expand=True)

# Ejecutar ventana
ventana.mainloop()
