from carta import Carta
import random


class Mazo():
    def __init__(self) -> None:
        self.__cartas = []  
        self.__cartas_genericas = []

    @property
    def cartas_genericas(self):
        self.__cartas_genericas = sorted(self.__cartas_genericas, key=lambda x: x.jerarquia, reverse=True)
        return self.__cartas_genericas

    @cartas_genericas.setter
    def cartas_genericas(self, new_cartas_genericas):
        self.__cartas_genericas = new_cartas_genericas

    @property
    def cartas(self):
        return self.__cartas

    @cartas.setter
    def cartas(self, new_cartas):
        self.__cartas = new_cartas

    # METODOS

    def __str__(self) -> str:
        return f"{self.cartas}\n"

    def remove_cartas(self, carta: Carta):
        self.cartas.remove(carta)

    def reset_mazo(self):
        self.cartas.clear()
        self.cartas.extend(self.cartas_genericas)

    def crear_mazo(self, cartas: list):
        self.cartas.extend(cartas)
        self.cartas_genericas.extend(cartas)

    def barajar(self):
        self.reset_mazo()
        random.shuffle(self.cartas)
    
    def repartir(self) -> list: 
        cartas = []
        from generador_carta import Generador_cartas
        cartas = Generador_cartas.generar_carta(self)

        return cartas
    
        
        


