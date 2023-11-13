from config.conexionBd import Conexion

class ContactosService():
    def __init__(self):
        self.repository = Conexion()

    def consultarContactosNombre(self, nombre, idUsuario):
        sql = "SELECT c.nombreContacto, c.numeroTelefono FROM contactos c WHERE c.nombreContacto LIKE %s and c.idUsuario = %s"
        self.repository.cursor.execute(sql, (f'%{nombre}%', idUsuario))
        resultados = self.repository.cursor.fetchall()
        return resultados

    def consultarContactosAll(self, idUsuario):
        sql = "SELECT c.nombreContacto, c.numeroTelefono FROM contactos c WHERE c.idUsuario = %s"
        self.repository.cursor.execute(sql, (idUsuario,))
        resultados = self.repository.cursor.fetchall()
        return resultados
