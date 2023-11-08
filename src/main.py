from view import App
from config.conexionBd import Conexion

def main():
    conexion = Conexion()
    conexion.crearBd()
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()