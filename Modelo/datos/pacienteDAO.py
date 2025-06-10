import sqlite3

# Conexión a una base de datos (se crea si no existe)
conexion = sqlite3.connect('/DataBases/Hospital.db')

# Crear un cursor para ejecutar sentencias SQL
cursor = conexion.cursor()

# Crear una tabla (si no existe)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS "Pacientes" ( 
               "id" TEXT NOT NULL UNIQUE, 
               "nombre" TEXT NOT NULL, 
               "edad" INTEGER NOT NULL, 
               "genero" TEXT NOT NULL, 
               "motivo" TEXT NOT NULL, 
               "gravedad" INTEGER NOT NULL, 
               "fechadeingreso" TEXT NOT NULL, 
               "atendido" INTEGER NOT NULL, PRIMARY KEY("id") 
    );''')

class PacienteDAO:

    #Insertar datos del paciente a la base de datos.
    @staticmethod
    def insertarPaciente(idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido):
        cursor.execute('''
            INSERT INTO Pacientes (id, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (idPaciente, nombre, edad, genero, motivo, gravedad, fechadeingreso, atendido))
        conexion.commit()
    