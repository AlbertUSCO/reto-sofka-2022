from typing import List


class Pregunta:

    def __init__(self, ronda: int = 0, sentencia: str = None, opciones: List[str] = None, respuesta: str = None) -> None:
        self.rondas = ronda
        self.sentencia = sentencia
        self.opciones = opciones
        self.respuesta = respuesta

    def generar_pregunta(self, pregunta_dataframe):
        self.sentencia = pregunta_dataframe["pregunta"].values[0]
        self.opciones = [pregunta_dataframe["a"].values[0], pregunta_dataframe["b"].values[0],
                         pregunta_dataframe["c"].values[0], pregunta_dataframe["d"].values[0]]
        self.respuesta = pregunta_dataframe["respuesta"].values[0]
