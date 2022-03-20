from typing import List
import pandas as pd

from preguntas import Pregunta


class BaseDatos:

    def __init__(self) -> None:
        self.base_datos = pd.read_csv('..\\resources\\Preguntas.csv', sep=';')

    def filtrar_por_ronda(self, ronda: int):
        return self.base_datos[self.base_datos['categoria'] == ronda]

    def seleccionar_pregunta(self, ronda_pregunta: int) -> Pregunta:
        pregunta_seleccionada = Pregunta(ronda=ronda_pregunta)
        pregunta_base = self.filtrar_por_ronda(ronda_pregunta).sample()
        pregunta_seleccionada.generar_pregunta(pregunta_base)

        return pregunta_seleccionada
