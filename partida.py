from ronda import Ronda
from jugador import Jugador
from carta import Carta
from mano import Mano



class Partida():

   

    def __init__(self) -> None:
        self.__rondas = []
        

    @property
    def jugadores(self):
        return self.__jugadores
    
    @jugadores.setter
    def jugadores(self, new_jugadores):
        self.__jugadores = new_jugadores

    @property
    def rondas(self):
        return self.__rondas
    
    @rondas.setter
    def rondas(self, new_rondas):
        self.__rondas = new_rondas


    def __str__(self) -> str:
        return self.rondas[0]

    def iniciar_ronda(self, ronda:Ronda):
         self.rondas.append(ronda)

    def determinar_ganador(self): 
        self.rondas[0].determinar_ganador()     
        if self.rondas[0].mano.jugador_1.rondas_ganadas == 15:
            return self.rondas[0].mano.jugador_1
        elif self.rondas[0].mano.jugador_2.rondas_ganadas == 15:
            return self.rondas[0].mano.jugador_2
        else:
            pass
        

