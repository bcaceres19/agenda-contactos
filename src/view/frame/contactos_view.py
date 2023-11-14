import customtkinter as ctk
from config.configViews import Configuracion
from ..widgets.tabla import Tabla
from ..widgets.boton import Boton
from ..widgets.campo_texto import CampoTexto
from controller.contactoController import ContactoController
from CTkMessagebox import CTkMessagebox


class Contactos(ctk.CTkFrame):
    def __init__(self, master,idUsuario,**kwargs):
        super().__init__(master, **kwargs)
        self.contacto = ContactoController()
        config = Configuracion().config
        self.usuario = idUsuario
        infotTextos = config["vistaContactos"]["textoC"]
        infoCabeceraT = config["vistaContactos"]["cabeceraT"]
        infoBoton = config["vistaContactos"]["botones"]
        infoCampoT = config["vistaContactos"]["campoTexto"]
        self.infoMensajes = config["vistaContactos"]["ventanaMensaje"][0]
        self.campos = []

        for campo in infoCampoT:
            self.campos.append(CampoTexto(self, campo))

        #CABECERA
        self.tabla = Tabla(self,informacion=infotTextos, cabecera=infoCabeceraT)

        self.contenidoTabla(self.tabla, False)

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
        self.contenidoTabla(self.tabla, True)

    def contenidoTabla(self,tabla, query):
        if(not query):
            self.infoContenidoT = self.dataTablaAll(self.usuario)
        for info in self.infoContenidoT:
            tabla.contenido((info[0], info[1]), info[2])
    
    def actualizarContacto(self):
        self.master.cambiarFrameModC(self.tabla.idContenido, self.usuario)

    def dataNombre(self):
        nombre = self.campos[0].tenerContenido()
        self.dataTablaNombre(nombre, self.usuario)

    def eliminarRegistro(self):
        self.contacto.eliminarContacto(self.tabla.idContenido)
        msg = CTkMessagebox(master=self,
                        title=self.infoMensajes["titulo"],
                        message=self.infoMensajes["texto"],
                        icon=self.infoMensajes["icono"]
                    )
        respuesta = msg.get()
        if(respuesta == "OK" or respuesta == None):
            self.limpiarTreeView(self.tabla)
            self.contenidoTabla(self.tabla, False)
        

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None