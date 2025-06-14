import tkinter as tk



class Login:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Login - Sistema hospitalario")
        ventana.geometry("400x300")
        ventana.configure(bg="#e1e1e1")

        # Colores
        color_azul = "#1f77b4"
        color_blanco = "#ffffff"
        color_gris = "#d3d3d3"

        # Título
        titulo = tk.Label(ventana, text="Sistema Hospitalario", font=("Helvetica", 16, "bold"),
                          bg="#f0f0f0", fg=color_azul)
        titulo.pack(pady=20)

        # Frame formulario
        frame = tk.Frame(ventana, bg=color_blanco, bd=2, relief="groove")
        frame.pack(padx=30, pady=10)

        # Usuario
        tk.Label(frame, text="Nombre de usuario:", bg=color_blanco).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_usuario = tk.Entry(frame, width=25)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=10)

        # Contraseña
        tk.Label(frame, text="Contraseña:", bg=color_blanco).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.entry_contrasena = tk.Entry(frame, show="*", width=25)
        self.entry_contrasena.grid(row=1, column=1, padx=10, pady=10)

        # Botón Login
        boton_login = tk.Button(ventana, text="Iniciar sesión", bg=color_azul, fg=color_blanco, width=20, command=self.iniciar_sesion)
        boton_login.pack(pady=10)

        # Botón Registro
        boton_registro = tk.Button(ventana, text="Registrarse", bg=color_gris, width=20, command=self.registrarse)
        boton_registro.pack()

    def iniciar_sesion(self):
        from Controlador.loginControlador import LoginControlador
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        LoginControlador.iniciar_sesion(usuario, contrasena)

    def registrarse(self):
        from Vista.gui.vent_reg_us import ventanaRegistroUsuario 
        self.ventana.destroy()
        ventanaRegistroUsuario(tk.Tk()).mostrar()
       
        
    def mostrar(self):
        self.ventana.mainloop()