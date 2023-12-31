import customtkinter as ctk
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from ..widgets.texto import Texto
from config.configViews import Configuracion
from controller.contactoController import ContactoController
from CTkMessagebox import CTkMessagebox

class Modificar(ctk.CTkFrame):
    def __init__(self, master,idContacto,idUsuario,**kwargs):
        super().__init__(master, **kwargs)
        self.contacto = ContactoController()
        self.idUsuario = idUsuario
        config = Configuracion().config
        self.idContacto = idContacto
        infotTextos = config["vistaModificar"]["textos"]
        botones = config["vistaModificar"]["botones"]
        infoCampos = config["vistaModificar"]["camposTexto"]
        self.infoMensajes = config["vistaModificar"]["ventanaMensaje"]

        self.campos = []
        infoContacto = self.informacionId()
        self.numero = infoContacto[0][1]    

        for texto in infotTextos:
            Texto(self,informacion=texto)

        for campo, info in zip(infoCampos,infoContacto[0]):
           campo["contenido"] = info
           self.campos.append(CampoTexto(self, informacion=campo))

        for boton in botones:
            Boton(self, informacion=boton)
        
    def modificar(self):
        campo = self.campos[0]
        nombre = self.campos[0].tenerContenido()
        numero = self.campos[1].tenerContenido()
        informacion = {}
        if(campo.validarNombreCont(nombre)):
            if(campo.validarNumero(numero)):
                existe = False
                if self.numero != numero:
                    existe = self.contacto.bucarNumero(numero, self.idUsuario)
                if not existe:
                    informacion["nombre"] = nombre
                    informacion["numero"] = numero
                    informacion["id"] = self.idContacto
                    self.contacto.modificarContacto(informacion)
                    msg = CTkMessagebox(master=self,
                            title=self.infoMensajes[0]["titulo"],
                            message=self.infoMensajes[0]["texto"],
                            icon=self.infoMensajes[0]["icono"]
                        )
                    respuesta = msg.get()
                    if(respuesta == "OK" or respuesta == None):
                        self.master.cambiarFrameContactos(self.idUsuario)
                else:
                    CTkMessagebox(master=self,
                            title=self.infoMensajes[1]["titulo"],
                            message=self.infoMensajes[1]["texto"],
                            icon=self.infoMensajes[1]["icono"]
                        )

    def informacionId(self):
        return self.contacto.consultarContactoId(idContacto=self.idContacto)

    def frameContactos(self):
        self.master.cambiarFrameContactos(self.idUsuario)

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None       