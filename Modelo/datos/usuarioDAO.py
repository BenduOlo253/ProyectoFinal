import sqlite3
import os

class UsuarioDAO:

    @staticmethod
    def __obtenerConexion():
        ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'Hospital.db'))
        return sqlite3.connect(ruta_db)

    @staticmethod
    def __crearTabla(cursor):
        cursor.execute('''
                       CREATE TABLE "Usuarios" ( 
                       "id" TEXT NOT NULL UNIQUE, 
                       "nombre" TEXT NOT NULL UNIQUE, 
                       "contraseña" TEXT NOT NULL, 
                       "rol" TEXT NOT NULL, PRIMARY KEY("id") );
            );
        ''')

    @staticmethod
    def  obtenerUsuarios():
        conn = UsuarioDAO.__obtenerConexion()
        cursor = conn.cursor()
        UsuarioDAO.__crearTabla(cursor)
        cursor.execute('SELECT * FROM Usuarios')
        filas = cursor.fetchall()
        conn.close()
        return filas
    
    @staticmethod
    def insertarUsuario(idUsuario, nombre, contraseña, rol):
        conn = UsuarioDAO.__obtenerConexion()
        cursor = conn.cursor()
        UsuarioDAO.__crearTabla(cursor)
        cursor.execute('''
            INSERT INTO Usuarios (id, nombre, contraseña, rol)
            VALUES (?, ?, ?, ?)
        ''', (idUsuario, nombre, contraseña, rol))
        conn.commit()
        conn.close()

    @staticmethod
    def actualizarUsuario(idUsuario, nombre, contraseña, rol):
        conn = UsuarioDAO.__obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Usuarios
            SET nombre = ?, contraseña = ?, rol = ?
            WHERE id = ?''', (nombre, contraseña, rol, idUsuario))
        conn.commit()
        conn.close()
    
    @staticmethod
    def eliminarPaciente(idUsuario):
        conn = UsuarioDAO.__obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Usuario WHERE id = ?', (idUsuario))
        conn.commit()
        conn.close()