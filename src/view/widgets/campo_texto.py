from customtkinter import CTkFont,CTkEntry, CTkImage
from PIL import Image
from CTkMessagebox import CTkMessagebox
import re

class CampoTexto(CTkEntry):
    def __init__(self, master, informacion, **kwargs):
        super().__init__(master,**kwargs)
      
        self.configure(
            placeholder_text=informacion.get("texto"),
            fg_color=informacion.get("fondoColor"), 
            text_color=informacion.get("textColor"), 
            border_color=informacion.get("bordeColor"), 
            width=informacion.get("ancho"), 
            height=informacion.get("alto"), 
            corner_radius=informacion.get("redondeo"),
            font=CTkFont(size=informacion.get("tamañoLetra"), family=informacion.get("tipoLetra")),
            show = informacion.get("tipo"),
            validatecommand=(self.getComando(informacion.get("comandoValidador")), "%P")
            )
        
        
        if "contenido" in informacion:
            self.insert(0,informacion["contenido"])

        self.grid(row=informacion.get("fila"), column=informacion.get("columna"), pady=3)
    

    def tenerContenido(self):
        return self.get()
    
    def validarEmail(self,correo):
        if correo:
            if correo is  not  None and len(correo) < 250:
                patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                if re.match(patron, correo):
                    return True
                else:
                    CTkMessagebox(master=self.master,title="Error", message="Ingresa una dirección de correo electrónico válida", icon="cancel")
                    return False
            else:
                CTkMessagebox(master=self.master,title="Error", message="El correo supera los 250 caracteres, ingresa un nombre valido", icon="cancel")
                return False
        else:
            CTkMessagebox(master=self.master,title="Error", message="El campo del correo esta vacio, llenalo porfavor", icon="cancel")
            return False

    def validarPasswords(self, passwordUno, passwordDos):
        if passwordUno and passwordDos:

            if passwordUno == passwordDos:
                return True
            else:
                CTkMessagebox(master=self.master,title="Error", message="Las contraseñas son distintas, asegurate de que sean iguales", icon="cancel")
                return False
        else:
            CTkMessagebox(master=self.master,title="Error", message="Alguno de las dos contraseñas esta vacia, llenalo porfavor.", icon="cancel")
            return False
        
    def validarNumero(self, numero):
        if numero:
            if numero is not None and len(numero) < 11:
                return True
            else:
                CTkMessagebox(master=self.master,title="Error", message="El numero de telefono supera los 11 caracteres, ingresa un numero valido", icon="cancel")
                return False
        else:
            CTkMessagebox(master=self.master,title="Error", message="El campo numero esta vacio, llenalo porfavor", icon="cancel")
            return False
    def validarNombreCont(self, nombre):
        if nombre:

            if  nombre is not None and len(nombre) < 250:
                return True
            else:
                CTkMessagebox(master=self.master,title="Error", message="El nombre del contacto supera los 250 caracteres, ingresa un nombre valido", icon="cancel")
                return False
        else:
            CTkMessagebox(master=self.master,title="Error", message="El campo nombre del contacto esta vacio, llenalo porfavor", icon="cancel")
            return False
        
    def eliminarContenido(self):
        self.delete(0,'end')

    def getComando(self, comando):
        if hasattr(self, comando):
            return getattr(self, comando)
        else:
            return None
