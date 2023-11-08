import customtkinter
from .frame.registro_view import Registro
from screeninfo import get_monitors
from config.configViews import Configuracion

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        config  = Configuracion().config            
        root = config["root"]
        frame = config["root"]["configFrame"]
        anchoPantalla = self.informacionMonitor().get("ancho")
        print(anchoPantalla)
        altoPantalla = self.informacionMonitor().get("alto")
        print(altoPantalla)
        self.geometry(f"{anchoPantalla}x{altoPantalla}")
        self.configure(fg_color=root.get("fondoRoot"))
        self.frameRegistro = Registro(
            master=self, 
            width=frame.get("ancho"), 
            height=frame.get("alto"), 
            fg_color=frame.get("fondoColor"), 
            border_color=frame.get("bordeColor")
            )

        self.frameRegistro.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def informacionMonitor(self):
        pantallas = get_monitors()
        monitor = pantallas[-1]
        infoPantalla = {"ancho": monitor.width, "alto": monitor.height}
        return infoPantalla