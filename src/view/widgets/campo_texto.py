from customtkinter import CTkFont,CTkEntry, CTkImage
from PIL import Image

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
            )
        
        self.grid(row=informacion.get("fila"), column=informacion.get("columna"), pady=3)
    

    def tenerContenido(self):
        return self.get()
