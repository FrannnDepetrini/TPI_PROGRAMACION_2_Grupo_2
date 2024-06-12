


class Ronda():

    def __init__(self, ganador) -> None:
        self.__ganador = ganador #Jugador
        self.__manos = [] #List[Mano]


    @property
    def ganador(self):
        return self.__ganador

    @ganador.setter
    def ganador(self, new_ganador):
        self.__ganador = new_ganador

    @property
    def manos(self):
        return self.__manos


    



    # METODOS


    def iniciar_mano(): #Mano
        pass

    def determinar_ganador():
        pass