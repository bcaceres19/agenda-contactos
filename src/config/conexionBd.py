import os
import configparser
import mysql.connector

class Conexion:
    def __init__(self, config=None):
        if config is None:
            config_path = os.path.abspath('config.ini')
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
    
    def crearBd(self):
        consultaBd = "SHOW DATABASES LIKE 'agenda'"
        self.cursor.execute(consultaBd)
        # Recupera los resultados
        bd_existe = self.cursor.fetchone()
        if not bd_existe:
            crear_base_de_datos = "CREATE DATABASE agenda"
            self.cursor.execute(crear_base_de_datos)

            self.cursor.execute("USE agenda")
            with open('src/util/bd.sql', 'r') as sql_file:
                sql_script = sql_file.read()
            self.cursor.execute(sql_script)        
        self.conexion.commit()
        self.cerrar()


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