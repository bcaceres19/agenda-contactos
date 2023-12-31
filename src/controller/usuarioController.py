from service.usuariosService import UsuariosService

class UsuarioController():
    def __init__(self):
        self.usuario = UsuariosService()

    def crearUsuario(self, data):
        confirmacion = self.usuario.crearUsuario(data=data)
        return confirmacion
    
    def buscarEmailContra(self, email, contra):
         return self.usuario.buscarEmailContra(email, contra)
    
    def buscarEmail(self, email):
        return self.usuario.buscarEmail(email)