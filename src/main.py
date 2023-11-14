from view import App
from config.conexionBd import Conexion
from PIL import Image, ImageTk

def main():
    conexion = Conexion()
    if not conexion.buscarBd():
        conexion.crearBd()

    app = App()
    icono = Image.open("src/util/img/agenda-fin.ico")
    icono = ImageTk.PhotoImage(icono)
    app.iconphoto(True, icono)
    app.title("AGENDA")

    app.mainloop()

if __name__ == "__main__":
    main()