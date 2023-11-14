import os
import mysql.connector
import configparser

class Conexion:
    def __init__(self, config=None, database=None):
        if config is None:
            config_path = os.path.abspath('config.ini')
        else:
            config_path = os.path.abspath(config)
        self.config = config_path
        self.dbConfig = self.leerConfig()
        self.cursor = None
        self.conexion = None
        self.establecerConexion(database)

    def leerConfig(self):
        config = configparser.ConfigParser()
        config.read(self.config)
        return config['database']

    def buscarBd(self):
         consultaBd = "SHOW DATABASES LIKE 'agenda'"
         self.cursor.execute(consultaBd)
         return self.cursor.fetchone()

    def establecerConexion(self, database=None):
        try:
            self.conexion = mysql.connector.connect(
                host=self.dbConfig['host'],
                user=self.dbConfig['username'],
                password=self.dbConfig['password'],
                database=database
            )
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as err:
            print(err)

    def crearBd(self):
        try:
            # Establecer conexión sin base de datos para crear la base de datos 'agenda'
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS agenda")
            self.conexion.commit()
        except Exception as e:
            print(f"Error al crear la base de datos: {e}")
        finally:
            self.cerrar()

        # Establecer conexión con la base de datos 'agenda' para ejecutar scripts SQL
        try:
            self.establecerConexion(database='agenda')
            with open('src/util/bd.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            self.cursor.execute(sql_script)
            self.conexion.commit()
        except Exception as e:
            print(f"Error al ejecutar el script SQL: {e}")
        finally:
            self.cerrar()

    def establecerConexionSinBd(self):
        self.establecerConexion(database=None)

    def cerrar(self):
        try:
            if self.cursor is not None:
                self.cursor.close()
            if self.conexion is not None and self.conexion.is_connected():
                self.conexion.close()
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")
