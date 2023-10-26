import configparser
import mysql.connector

class Conexion:
    def __init__(self, config='config.ini'):
        self.config = config
        self.dbConfig = self.leerConfig()
        self.conexion = self.estConexion()

    def leerConfig(self):
        # Crear un objeto ConfigParser y leer la configuración desde el archivo config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['database']

    def estConexion(self):
        try:
            con = mysql.connector.connect(
                host = self.dbConfig['host'],
                user = self.dbConfig['username'],
                password= self.dbConfig['password'],
                database= self.dbConfig['database']
            )

            if con.is_connected():
                print("Conexion exitosa")
            return con
        except mysql.connector.Error as err:
            print(err)
    
    def cerrar(self):
        if self.conexion is not None and self.conexion.is_connected():
            self.conexion.close()