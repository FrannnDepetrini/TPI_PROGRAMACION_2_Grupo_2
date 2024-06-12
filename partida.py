
class Partida():

    __prox_num = 0

    def __init__(self, jugadores:list) -> None:
        self.__jugadores = jugadores
        self.__rondas = Partida.obtener_prox_num()

    @property
    def jugadores(self):
        return self.__jugadores
    
    @jugadores.setter
    def jugadores(self, new_jugadores):
        self.jugadores = new_jugadores

    @property
    def rondas(self):
        return self.__rondas
    
    @rondas.setter
    def rondas(self, new_rondas):
        self.rondas = new_rondas



    @classmethod
    def obtener_prox_num(cls):
        cls.__prox_num = cls.__prox_num + 1