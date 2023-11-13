import customtkinter as ctk
from config.configViews import Configuracion
from ..widgets.tabla import Tabla
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from controller.contactoController import ContactoController


class Contactos(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        self.contacto = ContactoController()

        config = Configuracion().config
        infotTextos = config["vistaContactos"]["textoC"]
        infoCabeceraT = config["vistaContactos"]["cabeceraT"]
        self.infoContenidoT = self.dataTablaAll(1)
        infoBoton = config["vistaContactos"]["botones"]
        infoCampoT = config["vistaContactos"]["campoTexto"]
        self.campos = []


        for campo in infoCampoT:
            self.campos.append(CampoTexto(self, campo))

        #CABECERA
        self.tabla = Tabla(self,informacion=infotTextos, cabecera=infoCabeceraT)

        self.contenidoTabla(self.tabla)

        for boton in infoBoton:
            Boton(self, informacion=boton)


    def limpiarTreeView(self, tree):
        for item in tree.get_children():
            tree.delete(item)

    def dataTablaAll(self, idUsuario):
        return self.contacto.consultarContactoAll(idUsuario=idUsuario)
    
    def dataTablaNombre(self, nombre,idUsuario):
        self.limpiarTreeView(self.tabla)
        self.infoContenidoT = self.contacto.consultarContactoNombre(nombre=nombre,idUsuario=idUsuario)
        self.contenidoTabla(self.tabla)

    def contenidoTabla(self,tabla):
        for info in self.infoContenidoT:
            tabla.contenido((info[0], info[1], None))

    def dataNombre(self):
        nombre = self.campos[0].tenerContenido()
        self.dataTablaNombre(nombre, 1)

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None