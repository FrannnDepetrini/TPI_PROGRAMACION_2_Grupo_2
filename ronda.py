class Ronda():


    

    def __init__(self, mano) -> None:
        self.__ganador = None #Jugador
        self.__mano =  mano
        


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

    



    # METODOS
    def __str__(self):
        return f"{self.nro_rondas}| {self.mano}"

   
    def determinar_ganador(self):
        
        
        if self.mano.jugador_1.manos_ganadas > 1:
            self.mano.jugador_1.rondas_ganadas = self.mano.jugador_1.rondas_ganadas + 1
            self.ganador = self.mano.jugador_1
            return self.mano.jugador_1
        elif self.mano.jugador_2.manos_ganadas > 1:
            self.ganador = self.mano.jugador_2
            self.mano.jugador_2.rondas_ganadas = self.mano.jugador_2.rondas_ganadas + 1
            return self.mano.jugador_2
        else:
            pass

        
        return self.ganador

            
    
    

