from base_datos import BaseDatos
from utilidades import Utilidades
from jugador import Jugador

inicial = 100
histParticipantes = []


class Interface:
    def __init__(self, jugador) -> None:
        self.jugador = jugador

    def mostrar_jugador(self) -> None:
        print("Hola " + self.jugador.nombre)

    def comenzar_juego(self) -> None:
        acumulado = 0

        for ronda in range(1, 6):
            self.jugador.ronda = ronda
            premio = inicial*ronda
            if ronda > 1:
                retiro = input("Desea continuar? 1.Si  2.No\n")
                retiro = Utilidades.es_numerico(retiro)
                if retiro == 1:
                    pass
                else:
                    print("Ha ganado ${}".format(acumulado))
                    break

            print("Pregunta por: ${}".format(premio))
            base_datos = BaseDatos()
            pregunta = base_datos.seleccionar_pregunta(ronda)
            print(pregunta.sentencia)
            print("a. "+pregunta.opciones[0])
            print("b. "+pregunta.opciones[1])
            print("c. "+pregunta.opciones[2])
            print("d. "+pregunta.opciones[3])
            self.respuesta_participante = input("Respuesta definitiva: ")
            if pregunta.respuesta[0] == self.respuesta_participante:
                print("Muy Bien! (っ▀¯▀)つ ")
                acumulado = acumulado+premio
                self.jugador.puntos = acumulado
                if ronda == 5:
                    print("Eres el feliz ganador!\n")
                    print("Total ganado: ", acumulado)
                else:
                    print("Sige!, solo llevas: ", acumulado)
            else:
                print("Perdiste! (╯°□°）╯︵ ┻━┻ ")
                break
        self.jugador.almacenar_historial()
