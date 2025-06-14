from Modelo.dominio.Usuario import Usuario
from structures.tablaHash import TablaHash
from structures.listaEnlazada import ListaEnlazada

class UsuarioDAO:
    def __init__(self):
        self.tabla = TablaHash()

    def insertarUsuario(self, usuario: Usuario):
        clave = usuario.getId()
        self.tabla.insertarValor(clave, usuario)

    def obtenerUsuarioPorId(self, idUsuario):
        return self.tabla.obtenerValor(idUsuario)

    def obtenerUsuarios(self):
        usuarios = ListaEnlazada()
        for lista in self.tabla.tabla:
            for nodo in lista:
                usuarios.insertar(nodo.clave, nodo.valor)
        return usuarios

    def actualizarUsuario(self, idUsuario, nombre, contraseña, rol):
        usuario = self.obtenerUsuarioPorId(idUsuario)
        if usuario:
            usuario.setNombre(nombre)
            usuario.setContraseña(contraseña)
            usuario.setRol(rol)
            self.tabla.insertar(idUsuario, usuario)  # Actualiza
            return True
        return False

    def eliminarUsuario(self, idUsuario):
        return self.tabla.eliminar(idUsuario)
