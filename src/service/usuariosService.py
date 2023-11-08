from config.conexion import Conexion

class UsuariosService():
    def __init__(self):
        self.repository = Conexion()

    def crearUsuario(self, data):
        sql = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
        valores = (data.get("email"), data.get("contra"))
        self.repository.cursor.execute(sql, valores)
        self.repository.conexion.commit()
        self.repository.cerrar()
        return "Usuario Creado"