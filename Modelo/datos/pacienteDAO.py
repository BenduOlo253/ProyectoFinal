import sqlite3
import os
class PacienteDAO():

    @staticmethod
    def __obtenerConexion():
        ruta_db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Data', 'Hospital.db'))
        return sqlite3.connect(ruta_db)

    @staticmethod
    def __crearTabla(cursor):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pacientes (
                id TEXT NOT NULL UNIQUE,
                nombre TEXT NOT NULL,
                edad INTEGER NOT NULL,
                genero TEXT NOT NULL,
                motivo TEXT NOT NULL,
                gravedad INTEGER NOT NULL,
                fechadeingreso TEXT NOT NULL,
                atendido INTEGER NOT NULL,
                PRIMARY KEY(id)
            );
        ''')

    @staticmethod
    def  obtenerPacientes():
        conn = PacienteDAO.__obtenerConexion()
        cursor = conn.cursor()
        PacienteDAO.__crearTabla(cursor)
        cursor.execute('SELECT * FROM Pacientes')
        filas = cursor.fetchall()
        conn.close()
        return filas
    
    @staticmethod
    def obtenerPacientesPorGravedad():
        conn = PacienteDAO.__obtenerConexion()
        cursor = conn.cursor()
        PacienteDAO.__crearTabla(cursor)

    
    @staticmethod
    def obtenerPacientePorId(idPaciente):
        conn = PacienteDAO.__obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Pacientes WHERE id = ?',(idPaciente))
        resultados = cursor.fetchall()
        conn.close()
        return resultados
        
    @staticmethod
    def insertarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido):
        conn = PacienteDAO.__obtenerConexion()
        cursor = conn.cursor()
        PacienteDAO.__crearTabla(cursor)
        cursor.execute('''
            INSERT INTO Pacientes (id, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (idPaciente, nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido))
        conn.commit()
        conn.close()

    @staticmethod
    def actualizarPaciente(nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido, idPaciente):
        conn = PacienteDAO.__obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Pacientes
            SET nombre = ?, edad = ?, genero = ?, motivo = ?, gravedad = ?, fechadeingreso = ?, atendido = ?
            WHERE id = ?''', (nombre, edad, genero, motivo, gravedad, fechaDeIngreso, atendido, idPaciente))
        conn.commit()
        conn.close()
    
    @staticmethod
    def eliminarPaciente(idPaciente):
        conn = PacienteDAO.__obtenerConexion()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Pacientes WHERE id = ?', (idPaciente))
        conn.commit()
        conn.close()