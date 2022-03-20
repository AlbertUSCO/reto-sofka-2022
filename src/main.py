import sys
from utilidades import Utilidades
from jugador import Jugador
from interface import Interface

opcion = 0
jugador = Jugador()
interface = Interface(jugador)


def participantes():
    print("\nListado de Participantes\n")


def iniciar_juego():
    jugador.ingresar_nombre()
    interface.mostrar_jugador()
    interface.comenzar_juego()


def main():

    while True:
        print("\n")
        print("||¯\_(ツ)_/¯ - (งツ)ว - ʕ •́؈•̀ ₎|| -\n ")
        print("||      Listo para jugar?     ||\n")
        print("||(⊃｡•́‿•̀｡)⊃ - ʕ•ᴥ•ʔ - ƪ(ړײ)  ||\n")
        print("Selecciona una  opcion:\n")
        print("1. Iniciar")
        print("2. Ver historial de participantes")
        print("3. Salir")

        opcion = input("\nOpcion: ")
        opcion = Utilidades.es_numerico(opcion)

        if opcion == 1:
            iniciar_juego()
        elif opcion == 2:
            print(jugador.historial_juego())
        elif opcion == 3:
            sys.exit()
        else:
            print("Ups!! No es una opcion (ง '̀-'́)ง")


if __name__ == '__main__':
    main()
