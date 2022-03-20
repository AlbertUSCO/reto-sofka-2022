import time


class Utilidades:

    @staticmethod
    def es_numerico(retiro):
        try:
            int(retiro)
            retiro = int(retiro)
            return retiro
        except ValueError:
            print("Ups!! No es una opcion (ง '̀-'́)ง")
            time.sleep(1)
            print("Sigue inentando ¯\_(⊙︿⊙)_/¯")
