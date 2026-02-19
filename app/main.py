import sys
from .bd import init_db
from .app_controlador import AppControlador


def main():
    init_db()

    controlador = AppControlador()
    sys.exit(controlador.iniciar())


if __name__ == "__main__":
    main()
