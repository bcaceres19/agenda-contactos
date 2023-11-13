import customtkinter as ctk
from config.configViews import Configuracion
from ..widgets.texto import Texto
from ..widgets.boton import Boton
from controller.contactoController import ContactoController


class Menu(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        self.contacto = ContactoController()
        config = Configuracion().config
        
        infotTextos = config["vistaMenu"]["textos"]
        infoBotones = config["vistaMenu"]["botones"]

        for texto in infotTextos:
            Texto(self,informacion=texto)
        for boton in infoBotones:
            Boton(self, informacion=boton)
        
    def data(self):
        pass

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None
   