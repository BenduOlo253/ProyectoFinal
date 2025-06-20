import tkinter as tk

class VentanaPrincipal:
    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        ventana.title("Sistema Hospitalario")
        ventana.geometry("400x450")
        ventana.configure(bg="#727272")

        azul = "#1f77b4"
        blanco = "#ffffff"

        frame_principal = tk.Frame(ventana, bg=blanco, bd=3, relief="groove")
        frame_principal.pack(padx=10, pady=15, fill='both') 
        
        label_bienvenida = tk.Label(
            frame_principal,
            text=f"Bienvenido, {usuario}",
            font=("Helvetica", 16, "bold"),
            bg=blanco,
            fg=azul
        )
        label_bienvenida.pack(pady=(10, 10))

        # Botones
        tk.Button(
            frame_principal, text="Registrar Paciente", font=("Helvetica", 13),
            bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
            bd=1, relief="groove", width=25, cursor="hand2",
            padx=10, pady=8, command= self.registrar_paciente
        ).pack(pady=5)

        tk.Button(
            frame_principal, text="Ver Pacientes por Gravedad", font=("Helvetica", 13),
            bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
            bd=1, relief="groove", width=25, cursor="hand2",
            padx=10, pady=8, command= self.ver_pacientes_por_gravedad
        ).pack(pady=5)

        tk.Button(
            frame_principal, text="Cerrar Sesión", font=("Helvetica", 13),
            bg=azul, fg=blanco, activebackground="#145a86", activeforeground=blanco,
            bd=1, relief="groove", width=25, cursor="hand2",
            padx=10, pady=8, command=self.cerrar_sesion
        ).pack(pady=10)

    def mostrar(self):
        self.ventana.mainloop()

    def registrar_paciente(self):
        from Vista.vent_regis import VentanaRegistroPaciente
        ventana_registro = tk.Tk()
        VentanaRegistroPaciente(ventana_registro, controlador=None).mostrar()  # Pasa controlador si tienes

    def ver_pacientes_por_gravedad(self):
        from Vista.vent_list_paci import VentanaListaPacientes
        ventana_lista = tk.Toplevel(self.ventana)
        VentanaListaPacientes(ventana_lista).mostrar()

    def cerrar_sesion(self):
        from Vista.vent_login import Login
        self.ventana.destroy()
        root_login = tk.Tk()
        Login(root_login).mostrar()
