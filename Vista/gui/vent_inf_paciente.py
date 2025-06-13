import tkinter as tk

def mostrar_info_paciente():
    ventana = tk.Tk()
    ventana.title("Información del Paciente")
    ventana.geometry("400x300")
    ventana.configure(bg="#e1e1e1")  # Fondo gris claro

    # Colores
    color_azul = "#1f77b4"
    color_blanco = "#ffffff"

    # Título
    titulo = tk.Label(ventana, text="Datos del Paciente", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg=color_azul)
    titulo.pack(pady=20)

    # Marco de contenido
    frame = tk.Frame(ventana, bg=color_blanco, bd=2, relief="groove")
    frame.pack(padx=30, pady=10, fill="both", expand=True)

    # Etiquetas y campos (vacíos)
    labels = ["ID:", "Nombre:", "Edad:", "Gravedad:"]
    entries = []

    for i, texto in enumerate(labels):
        label = tk.Label(frame, text=texto, bg=color_blanco)
        label.grid(row=i, column=0, padx=10, pady=10, sticky="e")

        entry = tk.Entry(frame, width=30, state="readonly")
        entry.grid(row=i, column=1, padx=10, pady=10)
        entries.append(entry)

    ventana.mainloop()

# Llamar a la ventana (para probar)
mostrar_info_paciente()
    