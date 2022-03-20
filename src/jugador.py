import csv
from datetime import datetime
import pandas as pd
from utilidades import Utilidades


class Jugador:
    def __init__(self, nombre='', puntos=0, ronda=0) -> None:
        self.nombre = nombre
        self.puntos = puntos
        self.ronda = ronda

    def ingresar_nombre(self):
        self.nombre = input('Escribe tu nombre: ')

    def actualizar(self):
        print('Nombre: {}  Puntuacion: {}'.format(self.nombre, self.puntos))

    def almacenar_historial(self):
        with open('..\\resources\\Historial.csv', 'a+', encoding='UTF8', newline='') as historial:
            writer = csv.writer(historial)

            writer.writerow(
                [datetime.now(), self.nombre, self.puntos, self.ronda])
        pass

    def historial_juego(self):

        historial_general = pd.read_csv(
            "..\\resources\\Historial.csv", sep=',')
        ver_historial_gral = input(
            "Desea ver el historial general? 1.Si  2.No\n")
        ver_historial_gral = Utilidades.es_numerico(ver_historial_gral)

        if ver_historial_gral == 1:
            return historial_general.tail()

        else:
            if self.nombre:
                historial_jugador = historial_general[historial_general["Nombre"] == self.nombre]

            if historial_jugador.empty:
                return "Aun no juegas "

            return historial_jugador.tail()
