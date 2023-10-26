from config import conexion

def main():
    dbConexion = conexion.Conexion()

    dbConexion.cerrar()

if __name__ == "__main__":
    main()