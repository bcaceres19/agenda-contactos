from service.contactosService import ContactosService


class ContactoController():
    def __init__(self):
        self.contacto = ContactosService()

    def consultarContactoAll(self, idUsuario):
        return self.contacto.consultarContactosAll(idUsuario)

    def consultarContactoNombre(self, nombre, idUsuario):
        return self.contacto.consultarContactosNombre(nombre, idUsuario)