
from carta import Carta

class Mazo():
    def __init__(self) -> None:
        self.__cartas = [] #List[Carta]
        self.__cartas_genericas = []






    @property
    def cartas_genericas(self):
        self.__cartas_genericas = sorted(self.__cartas_genericas, key = lambda x: x.jerarquia, reverse= True)
        return self.__cartas_genericas

    @cartas_genericas.setter
    def cartas_genericas(self, new_cartas_genericas):
        self.__cartas_genericas = new_cartas_genericas




    @property
    def cartas(self):
        self.__cartas = sorted(self.__cartas, key = lambda x: x.jerarquia, reverse= True)
        return self.__cartas
    @cartas.setter
    def cartas(self, new_cartas):
        self.__cartas = new_cartas
    

    # METODOS
    def __str__(self) -> str:
        return f"{self.cartas}\n"


    def remove_cartas(self, carta:Carta):
        self.cartas.remove(carta)
    def reset_mazo(self):
        self.cartas = self.cartas_genericas

    def crear_mazo(self, cartas:list):
        self.cartas.extend(cartas)
        self.cartas_genericas.extend(cartas)

    def barajar(self):
        pass #shuffle metodo python

    def repartir(self): #List[Carta]
        pass