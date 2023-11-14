import customtkinter as ctk
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from ..widgets.texto import Texto
from config.configViews import Configuracion
from controller.contactoController import ContactoController
from CTkMessagebox import CTkMessagebox


class RegistrarContacto(ctk.CTkFrame):
    def __init__(self, master,idUsuario,**kwargs):
        super().__init__(master, **kwargs)
        self.contacto =  ContactoController()
        config = Configuracion().config
        self.usuario = idUsuario
        infotTextos = config["vistaRegistroC"]["textos"]
        botones = config["vistaRegistroC"]["botones"]
        infoCampos = config["vistaRegistroC"]["camposTexto"]
        self.infoMensajes = config["vistaRegistroC"]["ventanaMensaje"]
        self.campos = []

        for texto in infotTextos:
            Texto(self,informacion=texto)

        for campo in infoCampos:
           self.campos.append(CampoTexto(self, informacion=campo))

        for boton in botones:
            Boton(self, informacion=boton)
        
    def registrarContacto(self):
        informacion = {}
        nombre = self.campos[0].tenerContenido()
        numero = self.campos[1].tenerContenido()

        if(self.campos[0].validarNombreCont(nombre)):
            if(self.campos[1].validarNumero(numero)):
                if not self.contacto.bucarNumero(numero, self.usuario):
                    informacion["nombre"] = nombre
                    informacion["numero"] = numero
                    informacion["idUsuario"] = self.usuario
                    self.contacto.registrarContacto(data=informacion)
                    self.campos[0].eliminarContenido()
                    self.campos[1].eliminarContenido()
                    msg = CTkMessagebox(master=self,
                            title=self.infoMensajes[0]["titulo"],
                            message=self.infoMensajes[0]["texto"],
                            icon=self.infoMensajes[0]["icono"]
                        )
                    respuesta = msg.get()
                    if(respuesta == "OK" or respuesta == None):
                        self.master.cambiarFrameContactos(idUsuario=self.usuario)
                else:
                    CTkMessagebox(master=self,
                            title=self.infoMensajes[1]["titulo"],
                            message=self.infoMensajes[1]["texto"],
                            icon=self.infoMensajes[1]["icono"]
                        )
    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None       