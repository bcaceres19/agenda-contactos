from customtkinter import CTkLabel, CTkFont, CTkImage
from PIL import Image

class Texto(CTkLabel):
    def __init__(self, master, informacion, **kwargs):
        super().__init__(master,**kwargs)
        if "texto" in informacion:
            self.llenarTexto(informacion=informacion)
        elif "imagen" in informacion:
            self.generarImagen(informacion)
        self.pack()
    
    def generarImagen(self, informacion):
        try:
            photo = CTkImage(light_image= Image.open(informacion.get("imagen")), size=(100,69))
            self.configure(image=photo, text="")
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    def llenarTexto(self,informacion):
        self.configure(
                fg_color=informacion.get("fondoColor"), 
                text_color=informacion.get("textColor"), 
                width=informacion.get("ancho"), 
                height=informacion.get("alto"),
                text=informacion.get("texto"),
                font=CTkFont(size=informacion.get("tamañoLetra"), family=informacion.get("tipoLetra"))
                )
