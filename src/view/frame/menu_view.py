import customtkinter as ctk
from config.configViews import Configuracion
from ..widgets.texto import Texto
from ..widgets.boton import Boton
from controller.contactoController import ContactoController


class Menu(ctk.CTkFrame):
    def __init__(self, master, idUsuario,**kwargs):
        super().__init__(master, **kwargs)
        self.contacto = ContactoController()
        config = Configuracion().config
        self.usuario= idUsuario
        infotTextos = config["vistaMenu"]["textos"]
        infoBotones = config["vistaMenu"]["botones"]

        for texto in infotTextos:
            Texto(self,informacion=texto)
        for boton in infoBotones:
            Boton(self, informacion=boton)
        
    def cambiarFrameIs(self):
        self.master.cambiarFrameIs()

    def cambiarFramReC(self):
        self.master.cambiarFrameRegC(idUsuario=self.usuario)

    def cambiarFrameContactos(self):
        self.master.cambiarFrameContactos(idUsuario=self.usuario)

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None
   