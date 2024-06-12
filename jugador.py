from carta import Carta


class Jugador():

    def __init__(self, nombre:str, puntos:int) -> None:
        self.__nombre = nombre
        self.__puntos = puntos
        self.__cartas = [] #List[Carta]

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def puntos(self):
        return self.__puntos

    @puntos.setter
    def puntos(self, new_puntos):
        self.__puntos = new_puntos

    @property
    def cartas(self):
        return self.__cartas


    

    # METODOS


    def jugar_carta() -> Carta: #Carta
        pass

    def recibir_carta(carta: Carta):
        pass

    def cantar_truco():
        pass

    def responder_truco():
        pass

    