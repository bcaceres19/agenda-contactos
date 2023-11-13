import customtkinter as ctk
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from ..widgets.texto import Texto
from config.configViews import Configuracion
from controller.usuarioController import UsuarioController

class Modificar(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)

        config = Configuracion().config
        
        infotTextos = config["vistaModificar"]["textos"]
        botones = config["vistaModificar"]["botones"]
        infoCampos = config["vistaModificar"]["camposTexto"]
        self.campos = []

        for texto in infotTextos:
            Texto(self,informacion=texto)

        for campo in infoCampos:
           self.campos.append(CampoTexto(self, informacion=campo))

        for boton in botones:
            Boton(self, informacion=boton)
        
    def modificar(self):
        usuario = UsuarioController()
        informacion = {}
        informacion["Nombre"] = self.campos[0].tenerContenido()
        informacion["Apellido"] = self.campos[1].tenerContenido()
        informacion["Telefono"] = self.campos[2].tenerContenido()
        print(usuario.crearUsuario(data=informacion))

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None       