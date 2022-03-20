class Jugador:
    def __init__(self,nombre='',puntos=0,ronda=0) -> None:
        self.nombre=nombre
        self.puntos=puntos
        self.ronda=ronda
        
    def ingresar_nombre (self):
        self.nombre=input('Escribe tu nombre: ')
        
    def actualizar(self):
        print('Nombre: {}  Puntuacion: {}'.format(self.nombre, self.puntos))
    
    def almacenas_historial(self):
        pass
        
    