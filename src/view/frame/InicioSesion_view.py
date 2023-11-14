import customtkinter as ctk
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from ..widgets.texto import Texto
from config.configViews import Configuracion
from controller.usuarioController import UsuarioController
from CTkMessagebox import CTkMessagebox


class InicioSesion(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        self.usuario = UsuarioController()

        config = Configuracion().config
        
        infotTextos = config["vistaInicioSesion"]["textos"]
        botones = config["vistaInicioSesion"]["botones"]
        infoCampos = config["vistaInicioSesion"]["camposTexto"]
        self.infoMensajes = config["vistaInicioSesion"]["ventanaMensaje"][0]
        self.campos = []

        for texto in infotTextos:
            Texto(self,informacion=texto)

        for campo in infoCampos:
           self.campos.append(CampoTexto(self, informacion=campo))

        for boton in botones:
            Boton(self, informacion=boton)
        
    def cambiarFrameRegistrar(self):
        self.master.cambiarFrameRegistroU()

    def iniciarSesion(self):
        email = self.campos[0].tenerContenido()
        contra = self.campos[1].tenerContenido()
        if(self.campos[0].validarEmail(email)):
            resultado = self.usuario.buscarEmailContra(email, contra)
            if not resultado:
                CTkMessagebox(master=self,
                    title=self.infoMensajes["titulo"],
                    message=self.infoMensajes["texto"],
                    icon=self.infoMensajes["icono"]
                    )
            else:   
                self.master.cambiarFrameContactos(idUsuario=resultado[0][0])

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None       