from customtkinter import CTkButton, CTkFont, CTkImage
from PIL import Image

class Boton(CTkButton):
    def __init__(self, master,informacion,**kwargs):
        super().__init__(master,**kwargs)
        photo=None
        if "imagen" in informacion:
            photo = CTkImage(light_image= Image.open(informacion.get("imagen")), size=(informacion.get("anchoImg"),informacion.get("altoImg")))
        self.configure(
            text=informacion.get("text"), 
            fg_color=informacion.get("fondoColor"), 
            text_color=informacion.get("textColor"), 
            border_color=informacion.get("bordeColor"), 
            width=informacion.get("ancho"), 
            height=informacion.get("alto"), 
            corner_radius=informacion.get("redondeo"),
            hover_color=informacion.get("fondoColorMouse"),
            font=CTkFont(size=informacion.get("tamañoLetra"), family=informacion.get("tipoLetra")),
            command=master.getComando(informacion.get("comando")),
            compound=informacion.get("direccionImg"), 
            image=photo,
            anchor=informacion.get("posicion")
            )
        self.grid(row=informacion.get("fila"), column=informacion.get("columna"), pady=informacion.get("y"), padx=informacion.get("x"),sticky=informacion.get("posicionB"))