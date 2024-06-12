from jugador import Jugador
from carta import Carta



class Mano():
    def __init__(self) -> None:
        self.__cartas_jugadas = []
    
    @property
    def cartas_jugadas(self):
        return self.__cartas_jugadas
    
    @cartas_jugadas.setter
    def cartas_jugadas(self, new_cartas_jugadas):
        self.cartas_jugadas = new_cartas_jugadas
      
    
    def jugar(self, jugador:Jugador, carta: Carta):
        pass

    def determinar_ganador(self):
        pass

    def __str__(self) -> str:
        return self.cartas_jugadas
