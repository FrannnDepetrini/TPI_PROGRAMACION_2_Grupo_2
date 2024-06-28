


class Jugador():

    def __init__(self, nombre:str,suTurno:bool= False) -> None:
        self.__nombre = nombre
        self.__cartas = [] 
        self.__manos_ganadas = 0
        self.__rondas_ganadas = 0
        self.__suTurno = suTurno
        


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre


    @property
    def cartas(self):
        return self.__cartas

    @cartas.setter
    def cartas(self, new_cartas):
        self.__cartas = new_cartas

    @property
    def manos_ganadas(self):
        return self.__manos_ganadas

    @manos_ganadas.setter
    def manos_ganadas(self, new_manos_ganadas):
        self.__manos_ganadas = new_manos_ganadas
    
    @property
    def rondas_ganadas(self):
        return self.__rondas_ganadas

    @rondas_ganadas.setter
    def rondas_ganadas(self, new_rondas_ganadas):
        self.__rondas_ganadas = new_rondas_ganadas

    @property
    def suTurno(self):
        return self.__suTurno

    @suTurno.setter
    def suTurno(self, new_suTurno):
        self.__suTurno = new_suTurno
   
   

    def __str__(self):
        return f"{self.nombre}"

    def tirar_carta(self, carta) :
        self.cartas.remove(carta)
        return carta
      

    



    def recibir_carta(self):
        from datos import mazo
        self.cartas.extend(mazo.repartir())

    

    