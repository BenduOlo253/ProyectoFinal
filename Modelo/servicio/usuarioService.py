from Modelo.datos.usuarioDAO import UsuarioDAO

class UsuarioService:

    @staticmethod
    def __verificarDuplicados(idUsuario):
        usuarios = UsuarioDAO.obtenerUsuarioPorId(idUsuario)
        if len(usuarios) == 0:
            return False
        else: return True

    @staticmethod
    def autenticarUsuario(idUsuario, contraseña):
        if len(UsuarioService.buscarUsuario(idUsuario)) < 1:
            return False
        elif (UsuarioService.buscarUsuario(idUsuario)[0])[2] == contraseña:
            return True
        else: return False
        
    @staticmethod
    def obtenerUsuarios():
        return UsuarioDAO.obtenerUsuarios()

    @staticmethod
    def buscarUsuario(idUsuario):
        return UsuarioDAO.obtenerUsuarioPorId(idUsuario)
    
    @staticmethod
    def registrarUsuario(idUsuario, nombre, contraseña, rol):
        if not UsuarioService.__verificarDuplicados(idUsuario):
            UsuarioDAO.insertarUsuario(idUsuario, nombre, contraseña, rol)
            return (f"El usuario {nombre} ha sido registrado correctamente.")
        else: return (f"El ID del usuario {nombre} ya existe. Por favor use un ID unico.")

    @staticmethod
    def actualizarUsuario(nombre, contraseña, rol, idUsuario):
        UsuarioDAO.actualizarUsuario(nombre, contraseña, rol, idUsuario)
        return (f"El usuario {nombre} ha sido actualizado correctamente.")
    
    @staticmethod
    def removerUsuario(idUsuario):
        UsuarioDAO.eliminarUsuario(idUsuario)
        return "El usuario ha sido eliminado correctamente."