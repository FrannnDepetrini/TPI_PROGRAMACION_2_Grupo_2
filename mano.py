from carta import Carta
from jugador import Jugador


class Mano():
  
    def __init__(self,jugador1, jugador2, cartas_jugadas:list) -> None:
        self.__jugador_1 = jugador1
        self.__jugador_2 = jugador2
        self.__cartas_jugadas = cartas_jugadas
        self.__ganador_mano = None


    @property
    def jugador_1(self):
        return self.__jugador_1
    
    @jugador_1.setter
    def jugador_2(self, new_jugador_2):
        self.__jugador_2 = new_jugador_2

    @property
    def jugador_2(self):
        return self.__jugador_2
    
    @jugador_2.setter
    def jugador_2(self, new_jugador_2):
        self.__jugador_2 = new_jugador_2


    @property
    def ganador_mano(self):
        return self.__ganador_mano
    
    @ganador_mano.setter
    def ganador_mano(self, new_ganador_mano):
        self.__ganador_mano = new_ganador_mano
    
    @property
    def cartas_jugadas(self):
        return self.__cartas_jugadas
    
    @cartas_jugadas.setter
    def cartas_jugadas(self, new_cartas_jugadas):
        self.__cartas_jugadas = new_cartas_jugadas
      
      
      
    
  

    def determinar_ganador(self) :
        # while jugador1.manosGanadas < 2 and jugador2.manosGanadas < 2:
        # self.manos_jugadas = self.manos_jugadas + 1
        if self.jugador_1.suTurno == True and self.cartas_jugadas[0].jerarquia > self.cartas_jugadas[1].jerarquia:
            self.ganador_mano = self.jugador_1
            self.jugador_1.suTurno = True
            self.jugador_2.suTurno = False
        elif  self.jugador_1.suTurno == False and self.cartas_jugadas[1].jerarquia > self.cartas_jugadas[0].jerarquia:
            self.ganador_mano = self.jugador_1
            self.jugador_1.suTurno = True
            self.jugador_2.suTurno = False
        elif self.jugador_2.suTurno == True and self.cartas_jugadas[0].jerarquia > self.cartas_jugadas[1].jerarquia:
            self.ganador_mano = self.jugador_2
            self.jugador_2.suTurno = True
            self.jugador_1.suTurno = False
        else:
            self.jugador_2.suTurno = True
            self.jugador_1.suTurno = False
            self.ganador_mano = self.jugador_2
            
        # if jugador1.manosGanadas == 2:
        #     self.ganador_mano = jugador1 
        # else: 
        #     self.ganador_mano = jugador2
        return self.ganador_mano



    def __str__(self):
        return f"{self.ganador_mano}"

jugador1 = Jugador('Francisco', True, True)
jugador2 = Jugador('RobotIA', False, False)

mano = Mano(jugador1, jugador2, [Carta('Espada', 1, 14), Carta('Basto', 1, 13) ])
# print(mano.jugador_1.suTurno)
# if (mano.jugador_1.suTurno == True and mano.cartas_jugadas[0].jerarquia > mano.cartas_jugadas[1].jerarquia):
#     print("hola")

# print(mano.determinar_ganador())
# print(jugador1)
# if (mano.determinar_ganador() == jugador1):
#     print("hola")
# elif (mano.determinar_ganador() == jugador2):
#     print("will")
# else:
#     print("ninguno")