from service.contactosService import ContactosService


class ContactoController():
    def __init__(self):
        self.contacto = ContactosService()

    def consultarContactoAll(self, idUsuario):
        return self.contacto.consultarContactosAll(idUsuario)

    def consultarContactoNombre(self, nombre, idUsuario):
        return self.contacto.consultarContactosNombre(nombre, idUsuario)
    
    def consultarContactoId(self, idContacto):
        return self.contacto.consultarContactoId(idContacto)
    
    def registrarContacto(self, data):
        return self.contacto.registrarContacto(data)

    def modificarContacto(self, data):
        return self.contacto.modificarContacto(data=data)
    
    def eliminarContacto(self, idContacto):
        self.contacto.eliminarContacto(idContacto)

    def bucarNumero(self, numero, idUsuario):
        return self.contacto.buscarNumero(numero, idUsuario)