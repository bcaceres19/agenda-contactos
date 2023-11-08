from customtkinter import CTkButton, CTkFont

class Boton(CTkButton):
    def __init__(self, master,informacion,**kwargs):
        super().__init__(master,**kwargs)
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
            command=master.getComando(informacion.get("comando"))
            )
        self.pack(padx=5, pady=5)