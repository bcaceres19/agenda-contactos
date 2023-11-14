import customtkinter as ctk
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from ..widgets.texto import Texto
from config.configViews import Configuracion
from controller.usuarioController import UsuarioController
from CTkMessagebox import CTkMessagebox


class Registro(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)

        config = Configuracion().config
        
        infotTextos = config["vistaRegistro"]["textos"]
        botones = config["vistaRegistro"]["botones"]
        infoCampos = config["vistaRegistro"]["camposTexto"]
        self.infoMensajes = config["vistaRegistro"]["ventanaMensaje"]
        self.campos = []

        for texto in infotTextos:
            Texto(self,informacion=texto)
        for campo in infoCampos:
           self.campos.append(CampoTexto(self, informacion=campo))

        for boton in botones:
            Boton(self, informacion=boton)
        
    def registrar(self):
        try:
            usuario = UsuarioController()
            informacion = {}
            email = self.campos[0].tenerContenido()
            passwordUno =  self.campos[1].tenerContenido()
            passwordDos =  self.campos[2].tenerContenido()
            if(self.campos[0].validarEmail(email)):
                existe = usuario.buscarEmail(email)
                if(not existe):
                    if(self.campos[1].validarPasswords(passwordUno, passwordDos)):
                        informacion["email"] = email
                        informacion["contra"] = passwordUno
                        idUsuario = usuario.crearUsuario(data=informacion)
                        msg = CTkMessagebox(master=self,
                            title=self.infoMensajes[0]["titulo"],
                            message=self.infoMensajes[0]["texto"],
                            icon=self.infoMensajes[0]["icono"]
                        )
                        respuesta = msg.get()
                        if(respuesta == "OK" or respuesta == None):
                            self.master.cambiarFrameContactos(idUsuario=idUsuario)
                else:
                    CTkMessagebox(master=self,
                        title=self.infoMensajes[1]["titulo"],
                        message=self.infoMensajes[1]["texto"],
                        icon=self.infoMensajes[1]["icono"]
                    )
        except Exception as e:
            print(e)
        
    
    def cambiarFrameIs(self):
        self.master.cambiarFrameIs()

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None


    