from customtkinter import CTkLabel, CTkFont, CTkImage
from PIL import Image

class Texto(CTkLabel):
    def __init__(self, master, informacion, **kwargs):
        super().__init__(master,**kwargs)
        if "texto" in informacion:
            self.llenarTexto(informacion=informacion)
        elif "imagen" in informacion:
            self.generarImagen(informacion)
        elif "textoT" in informacion:
            self.generarTabla(informacion)
        self.grid(row=informacion.get("fila"), column=informacion.get("columna"), pady=informacion.get("y"), padx=informacion.get("x"))

    def generarImagen(self, informacion):
        try:
            photo = CTkImage(light_image= Image.open(informacion.get("imagen")), size=(informacion.get("anchoImg"),informacion.get("altoImg")))
            self.configure(image=photo, text="")
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    def llenarTexto(self,informacion):
        photo=None
        if "imagen" in informacion:
            photo = CTkImage(light_image= Image.open(informacion.get("imagen")), size=(informacion.get("anchoImg"),informacion.get("altoImg")))
        self.configure(
                fg_color=informacion.get("fondoColor"), 
                text_color=informacion.get("textColor"), 
                width=informacion.get("ancho"), 
                height=informacion.get("alto"),
                text=informacion.get("texto"),
                font=CTkFont(size=informacion.get("tamañoLetra"), family=informacion.get("tipoLetra")),
                image=photo, 
                compound=informacion.get("direccionImg"),
                anchor=informacion.get("posicion")
            )

    def generarTabla(self, informacion):
        self.configure(
            text=informacion.get("textoT"),
            width=informacion.get("ancho"),
            relief="solid", 
            padx=informacion.get("textoX"), 
            pady=informacion.get("textoY")
        )