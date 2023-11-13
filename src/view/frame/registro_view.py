import customtkinter as ctk
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from ..widgets.texto import Texto
from config.configViews import Configuracion
from controller.usuarioController import UsuarioController

class Registro(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)

        config = Configuracion().config
        
        infotTextos = config["vistaRegistro"]["textos"]
        botones = config["vistaRegistro"]["botones"]
        infoCampos = config["vistaRegistro"]["camposTexto"]
        self.campos = []

        for texto in infotTextos:
            Texto(self,informacion=texto)
        for campo in infoCampos:
           self.campos.append(CampoTexto(self, informacion=campo))

        for boton in botones:
            Boton(self, informacion=boton)
        
    def registrar(self):
        usuario = UsuarioController()
        informacion = {}
        informacion["email"] = self.campos[0].tenerContenido()
        informacion["contra"] = self.campos[1].tenerContenido()
        print(usuario.crearUsuario(data=informacion))
        self.master.cambiarFrameContactos()

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None