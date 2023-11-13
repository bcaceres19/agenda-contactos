import customtkinter
from .frame.registro_view import Registro
from .frame.menu_view import Menu
from .frame.contactos_view import Contactos
from screeninfo import get_monitors
from config.configViews import Configuracion

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        config  = Configuracion().config            
        root = config["root"]
        self.frame = config["root"]["configFrame"]
        anchoPantalla = self.informacionMonitor().get("ancho")
        altoPantalla = self.informacionMonitor().get("alto")
        self.geometry(f"{anchoPantalla}x{altoPantalla}")
        self.configure(fg_color=root.get("fondoRoot"))
        self.frameRegistro = Registro(
            master=self, 
            width=self.frame.get("ancho"), 
            height=self.frame.get("alto"), 
            fg_color=self.frame.get("fondoColor"), 
            border_color=self.frame.get("bordeColor")
            )

        self.frameRegistro.grid(row=1, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
    def informacionMonitor(self):
        pantallas = get_monitors()
        monitor = pantallas[-1]
        infoPantalla = {"ancho": monitor.width, "alto": monitor.height}
        return infoPantalla
    
    def cambiarFrameMenu(self):
        self.frameMenu = Menu(
            master=self, 
            width=346.9, 
            height=660.85, 
            fg_color=self.frame.get("fondoColor"), 
            border_color=self.frame.get("bordeColor")
            )

        self.frameMenu.grid(row=1, column=0, sticky="w")
    
    def cambiarFrameContactos(self):
        self.frameRegistro.destroy()
        self.frameContacto = Contactos(
            master=self, 
            width=self.frame.get("ancho"), 
            height=self.frame.get("alto"),
            fg_color=self.frame.get("fondoColor"), 
            border_color=self.frame.get("bordeColor")
            )

        self.frameContacto.grid(row=1, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.cambiarFrameMenu()