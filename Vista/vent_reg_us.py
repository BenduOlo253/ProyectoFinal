import tkinter as tk
from Controlador.loginControlador import LoginControlador
class ventanaRegistroUsuario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.controlador = LoginControlador()
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

        # Campo ID Usuario
        label_id = tk.Label(frame, text="ID Usuario:", bg=color_blanco)
        label_id.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_id = tk.Entry(frame, width=25)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        # Campo Nombre
        label_nombre = tk.Label(frame, text="Nombre:", bg=color_blanco)
        label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_nombre = tk.Entry(frame, width=25)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        # Campo Contraseña
        label_contra = tk.Label(frame, text="Contraseña:", bg=color_blanco)
        label_contra.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.entry_contraseña = tk.Entry(frame, show="*", width=25)
        self.entry_contraseña.grid(row=2, column=1, padx=10, pady=10)

        # Campo Rol
        label_rol = tk.Label(frame, text="Rol:", bg=color_blanco)
        label_rol.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_rol = tk.Entry(frame, width=25)
        self.entry_rol.grid(row=3, column=1, padx=10, pady=10)

        # Botón de acción
        boton_registro = tk.Button(ventana, text="Registrar Usuario", bg=color_azul, fg=color_blanco, width=20, command=self.registrarUsuario)
        boton_registro.pack(pady=20)

        # Botón de cancelar
        boton_cancelar = tk.Button(ventana, text="Cancelar", bg="#d3d3d3", width=20, command=self.cancelar)
        boton_cancelar.pack(pady=10)

    def mostrar(self):
        self.ventana.mainloop()
        
    def cancelar(self):
        from Vista.vent_login import Login
        self.ventana.destroy()
        Login(tk.Tk()).mostrar()
        

    def registrarUsuario(self):
        
        id_usuario = self.entry_id.get()
        nombre = self.entry_nombre.get()
        contraseña = self.entry_contraseña.get()
        rol = self.entry_rol.get()

        self.controlador.registrarUsuario(id_usuario, nombre, contraseña, rol)
