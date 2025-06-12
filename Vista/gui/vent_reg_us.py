import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Usuario - Sistema Hospitalario")
ventana.geometry("450x400")
ventana.configure(bg="#e1e1e1")

# Colores
color_azul = "#1f77b4"
color_blanco = "#ffffff"

# Título
titulo = tk.Label(ventana, text="Registro de Usuario", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg=color_azul)
titulo.pack(pady=20)

# Marco de formulario
frame = tk.Frame(ventana, bg=color_blanco, bd=2, relief="groove")
frame.pack(padx=30, pady=10)

# Lista de campos
campos = [
    ("ID Usuario:", "idUsuario"),
    ("Nombre:", "nombre"),
    ("Contraseña:", "contraseña"),
    ("Rol:", "rol")
]

entries = {}

# Crear campos
for i, (label_text, key) in enumerate(campos):
    label = tk.Label(frame, text=label_text, bg=color_blanco)
    label.grid(row=i, column=0, padx=10, pady=10, sticky="e")

    if key == "contraseña":
        entry = tk.Entry(frame, width=25, show="*")  # Ocultar contraseña
    else:
        entry = tk.Entry(frame, width=25)

    entry.grid(row=i, column=1, padx=10, pady=10)
    entries[key] = entry

# Botón de acción (sin funcionalidad)
boton_registro = tk.Button(ventana, text="Registrar Usuario", bg=color_azul, fg=color_blanco, width=20)
boton_registro.pack(pady=20)

# Ejecutar ventana
ventana.mainloop()
