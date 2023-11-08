import os
import configparser
import mysql.connector

class Conexion:
    def __init__(self, config=None):
        if config is None:
            config_path = os.path.abspath('agenda-contactos/config.ini')
        else:
            config_path = os.path.abspath(config)
        self.config = config_path
        self.dbConfig = self.leerConfig()
        self.conexion, self.cursor = self.estConexion()

    def leerConfig(self):
        # Crear un objeto ConfigParser y leer la configuración desde el archivo config.ini
        config = configparser.ConfigParser()
        config.read(self.config)
        return config['database']

    def estConexion(self):
        try:
            con = mysql.connector.connect(
                host = self.dbConfig['host'],
                user = self.dbConfig['username'],
                password= self.dbConfig['password'],
                database= self.dbConfig['database']
            )
    
            cursor = con.cursor()
            return con, cursor
        except mysql.connector.Error as err:
            print(err)
    
    def cerrar(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conexion is not None and self.conexion.is_connected():
            self.conexion.close()