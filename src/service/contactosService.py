from config.conexionBd import Conexion

class ContactosService():
    def __init__(self):
        self.repository = Conexion(database='agenda')

    def consultarContactosNombre(self, nombre, idUsuario):
        sql = "SELECT c.nombreContacto, c.numeroTelefono, c.id FROM contactos c WHERE c.nombreContacto LIKE %s and c.idUsuario = %s"
        self.repository.cursor.execute(sql, (f'%{nombre}%', idUsuario))
        resultados = self.repository.cursor.fetchall()
        return resultados

    def consultarContactosAll(self, idUsuario):
        sql = "SELECT c.nombreContacto, c.numeroTelefono, c.id FROM contactos c WHERE c.idUsuario = %s"
        self.repository.cursor.execute(sql, (idUsuario,))
        resultados = self.repository.cursor.fetchall()
        return resultados
    
    def consultarContactoId(self, idContacto):
        sql = "SELECT c.nombreContacto, c.numeroTelefono FROM contactos c WHERE c.id = %s"
        self.repository.cursor.execute(sql, (idContacto,))
        resultados = self.repository.cursor.fetchall()
        return resultados

    def registrarContacto(self, data):
        sql = "INSERT INTO contactos (nombreContacto, numeroTelefono,  idUsuario) VALUES (%s, %s, %s)"
        self.repository.cursor.execute(sql, (data["nombre"],data["numero"], data["idUsuario"]))
        self.repository.conexion.commit()

    def modificarContacto(self, data):
        sql = "UPDATE contactos c SET c.nombreContacto = %s, c.numeroTelefono = %s where  c.id = %s"
        self.repository.cursor.execute(sql, (data["nombre"],data["numero"], data["id"]))
        self.repository.conexion.commit()

    def buscarNumero(self, numero, idUsuario):
        sql = "SELECT COUNT(*) FROM contactos c where c.numeroTelefono = %s and c.id = %s"
        self.repository.cursor.execute(sql, (numero,idUsuario))
        resultado = self.repository.cursor.fetchone()[0]
        return resultado > 0

    def eliminarContacto(self, idContacto):
        sql = "DELETE FROM contactos c WHERE c.id = %s"
        self.repository.cursor.execute(sql, (idContacto,))
        self.repository.conexion.commit()