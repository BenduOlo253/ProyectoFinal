from Modelo.datos.usuarioDAO import UsuarioDAO
from Modelo.dominio.Usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.usuarioDAO = UsuarioDAO()

    def __verificarDuplicados(self, idUsuario):
        usuario = self.usuarioDAO.obtenerUsuarioPorId(idUsuario)
        return usuario is not None

    def autenticarUsuario(self, idUsuario, contraseña):
        usuario = self.usuarioDAO.obtenerUsuarioPorId(idUsuario)
        if usuario and usuario.getContraseña() == contraseña:
            return True
        return False

    def obtenerUsuarios(self):
        return self.usuarioDAO.obtenerUsuarios()  # Retorna ListaEnlazada de Usuarios

    def buscarUsuario(self, idUsuario):
        return self.usuarioDAO.obtenerUsuarioPorId(idUsuario)

    def registrarUsuario(self, idUsuario, nombre, contraseña, rol):
        if not self.__verificarDuplicados(idUsuario):
            usuario = Usuario(idUsuario, nombre, contraseña, rol)
            self.usuarioDAO.insertarUsuario(usuario)
            return f"El usuario {nombre} ha sido registrado correctamente."
        else:
            return f"El ID del usuario {nombre} ya existe. Por favor use un ID único."

    def actualizarUsuario(self, idUsuario, nombre, contraseña, rol):
        usuario = self.usuarioDAO.obtenerUsuarioPorId(idUsuario)
        if usuario:
            usuario.setNombre(nombre)
            usuario.setContraseña(contraseña)
            usuario.setRol(rol)
            self.usuarioDAO.insertarUsuario(usuario)  # Reemplaza
            return f"El usuario {nombre} ha sido actualizado correctamente."
        else:
            return "Usuario no encontrado."

    def removerUsuario(self, idUsuario):
        eliminado = self.usuarioDAO.eliminarUsuario(idUsuario)
        if eliminado:
            return "El usuario ha sido eliminado correctamente."
        else:
            return "Usuario no encontrado."
