from jugador import Jugador
from mano import Mano
from carta import Carta
class Ronda():


    __prox_num = 0

    def __init__(self, mano) -> None:
        self.__ganador = None #Jugador
        self.__mano =  mano
        self.__nro_rondas = Ronda.obtener_prox_num()


    @property
    def ganador(self):
        return self.__ganador

    @ganador.setter
    def ganador(self, new_ganador):
        self.__ganador = new_ganador

    @property
    def manos(self):
        return self.__mano
    
    @manos.setter
    def mano(self, new_mano):
        self.__mano = new_mano

    @property
    def nro_rondas(self):
        return self.__nro_rondas
    



    # METODOS
    def __str__(self):
        return f"{self.mano}"

    def iniciar_mano(self, mano): #Mano
        self.mano = mano

    def determinar_ganador(self):
        if (self.mano.determinar_ganador() == self.mano.jugador_1):
             self.mano.jugador_1.manos_ganadas = self.mano.jugador_1.manos_ganadas + 1
        else:
             self.mano.jugador_2.manos_ganadas = self.mano.jugador_2.manos_ganadas + 1

        if self.mano.jugador_1.manos_ganadas == 1:
            self.mano.jugador_1.rondas_ganadas = self.mano.jugador_1.rondas_ganadas + 1
            self.ganador = self.mano.jugador_1
            return self.mano.jugador_1
        elif self.mano.jugador_2.manos_ganadas == 1:
            self.ganador = self.mano.jugador_2
            self.mano.jugador_2.rondas_ganadas = self.mano.jugador_2.rondas_ganadas + 1
            return self.mano.jugador_2
        else:
            pass

        return self.ganador

            
    @classmethod
    def obtener_prox_num(cls):
        cls.__prox_num = cls.__prox_num + 1

# jugador1 = Jugador('Francisco', True, True)
# jugador2 = Jugador('RobotIA',)


# ronda = Ronda(Mano(jugador1,jugador2, [Carta('Espada', 1, 14), Carta('Basto', 1, 13) ]))
# print(ronda.determinar_ganador())
# # print(ronda.mano.determinar_ganador())
# # print(ronda.mano.jugador_1.manos_ganadas)
# # print(ronda.mano.jugador_1.rondas_ganadas)
# # print(ronda.mano.jugador_2.manos_ganadas)
# # print(ronda.mano.jugador_2.rondas_ganadas)
# print(ronda)