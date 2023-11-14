import customtkinter
from .frame.registro_view import Registro
from .frame.menu_view import Menu
from .frame.contactos_view import Contactos
from .frame.InicioSesion_view import InicioSesion
from .frame.Modificar_view import Modificar
from .frame.registrar_contacto_view import RegistrarContacto
from screeninfo import get_monitors
from config.configViews import Configuracion

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        config  = Configuracion().config            
        root = config["root"]
        self.configFrame = config["root"]["configFrame"]
        anchoPantalla = self.informacionMonitor().get("ancho")
        altoPantalla = self.informacionMonitor().get("alto")
        self.geometry(f"{anchoPantalla}x{altoPantalla}")
        self.configure(fg_color=root.get("fondoRoot"))
        self.cambiarFrameIs()
       
   
    def informacionMonitor(self):
        pantallas = get_monitors()
        monitor = pantallas[-1]
        infoPantalla = {"ancho": monitor.width, "alto": monitor.height}
        return infoPantalla
    
    def cambiarFrameMenu(self, idUsuario):
        self.frameMenu = Menu(
            master=self, 
            width=346.9, 
            height=660.85, 
            fg_color=self.configFrame.get("fondoColor"), 
            border_color=self.configFrame.get("bordeColor"),
            idUsuario=idUsuario
            )

        self.frameMenu.grid(row=1, column=0, sticky="w")
    
    def cambiarFrameIs(self):
        if hasattr(self, 'frameMenu'):
            self.frameMenu.destroy()
            self.frame.destroy()
        self.frame = InicioSesion(
            master=self, 
            width=self.configFrame.get("ancho"), 
            height=self.configFrame.get("alto"), 
            fg_color=self.configFrame.get("fondoColor"), 
            border_color=self.configFrame.get("bordeColor")
            )

        self.frame.grid(row=1, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def cambiarFrameRegistroU(self):
        self.frame.destroy()
        self.frame = Registro(
          master=self, 
            width=self.configFrame.get("ancho"), 
            height=self.configFrame.get("alto"),
            fg_color=self.configFrame.get("fondoColor"), 
            border_color=self.configFrame.get("bordeColor")  
        )
        self.frame.grid(row=1, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def cambiarFrameRegC(self, idUsuario):
        self.frame.destroy()
        self.frame = RegistrarContacto(
          master=self, 
            width=self.configFrame.get("ancho"), 
            height=self.configFrame.get("alto"),
            fg_color=self.configFrame.get("fondoColor"), 
            border_color=self.configFrame.get("bordeColor"), 
            idUsuario=idUsuario
        )
        self.frame.grid(row=1, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def cambiarFrameModC(self, idContacto, idUsuario):
        self.frame.destroy()
        self.frame = Modificar(
          master=self, 
            width=self.configFrame.get("ancho"), 
            height=self.configFrame.get("alto"),
            fg_color=self.configFrame.get("fondoColor"), 
            border_color=self.configFrame.get("bordeColor"),
            idContacto = idContacto,
            idUsuario=idUsuario
        )
        self.frame.grid(row=1, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


    def cambiarFrameContactos(self, idUsuario):
        self.frame.destroy()
        self.frame = Contactos(
            master=self, 
            width=self.configFrame.get("ancho"), 
            height=self.configFrame.get("alto"),
            fg_color=self.configFrame.get("fondoColor"), 
            border_color=self.configFrame.get("bordeColor"),
            idUsuario=idUsuario
            )

        self.frame.grid(row=1, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=2)
        if hasattr(self, 'frameMenu'):
            if not self.frameMenu.winfo_exists():
                self.cambiarFrameMenu(idUsuario=idUsuario)
        else:
            self.cambiarFrameMenu(idUsuario=idUsuario)

