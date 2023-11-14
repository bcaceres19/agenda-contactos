from config.conexionBd import Conexion

class UsuariosService():
    def __init__(self):
        self.repository = Conexion(database='agenda')

    def crearUsuario(self, data):
        sql = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"
        valores = (data.get("email"), data.get("contra"))
        self.repository.cursor.execute(sql, valores)
        self.repository.conexion.commit()
        id = self.repository.cursor.lastrowid
        return id
    
    def buscarEmailContra(self, email, contra):
        sql = "SELECT u.id FROM usuarios u WHERE u.email = %s and u.password = %s"
        self.repository.cursor.execute(sql, (email,contra))
        resultados = self.repository.cursor.fetchall()
        return resultados
    
    def buscarEmail(self,email):
        sql = "SELECT COUNT(*) FROM usuarios u where u.email = %s"
        self.repository.cursor.execute(sql, (email,))
        resultado = self.repository.cursor.fetchone()[0]
        return resultado > 0

     