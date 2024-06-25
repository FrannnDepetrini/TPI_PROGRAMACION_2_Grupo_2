
class Mano():

    __prox_nro = int(0)
    __es_mano = None
    __ganadorPrimera = None
    __huboParda = False
  
    def __init__(self,jugador1, jugador2, cartas_jugadas:list) -> None:
        self.__jugador_1 = jugador1
        self.__jugador_2 = jugador2
        self.__cartas_jugadas = cartas_jugadas
        self.__ganador_mano = None
        self.__nro = Mano.contador()
        


    @property
    def nro(self):
        return self.__nro    

   
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
      
    @property
    def huboParda(self):
        return self.__huboParda
         
    @property
    def ganadorPrimera(self):
        return self.__ganadorPrimera
                 
    @property
    def es_mano(self):
        return self.__es_mano
    
    @classmethod
    def contador(cls):
        cls.__prox_nro = cls.__prox_nro + 1
        if cls.__prox_nro > 3:
               cls.__prox_nro = 1
        return cls.__prox_nro
    
    
    def __str__(self):
        return f"{self.ganador_mano}"

    def determinar_ganador(self) :
        if self.jugador_1.manos_ganadas == 0 and self.jugador_2.manos_ganadas == 0:
            if self.jugador_1.suTurno:
                Mano.__es_mano = self.jugador_1
            else:
                Mano.__es_mano = self.jugador_2
 
        if self.jugador_1.suTurno == True and self.cartas_jugadas[0].jerarquia > self.cartas_jugadas[1].jerarquia:
            self.ganador_mano = self.jugador_1
            self.jugador_1.suTurno = True
            self.jugador_2.suTurno = False
            self.jugador_1.manos_ganadas = self.jugador_1.manos_ganadas + 1
            if self.nro == 1:
                Mano.__ganadorPrimera = self.jugador_1
            if Mano.__huboParda == True and self.nro == 2 or self.nro == 3 :
                self.jugador_1.manos_ganadas = 2
                self.limpiar()
                pass
            Mano.__huboParda = False
        elif  self.jugador_1.suTurno == False and self.cartas_jugadas[1].jerarquia > self.cartas_jugadas[0].jerarquia:
            self.ganador_mano = self.jugador_1
            self.jugador_1.suTurno = True
            self.jugador_2.suTurno = False
            self.jugador_1.manos_ganadas = self.jugador_1.manos_ganadas + 1
            if self.nro == 1:
                Mano.__ganadorPrimera = self.jugador_1
            if Mano.__huboParda == True and self.nro == 2 or self.nro == 3 :
                self.jugador_1.manos_ganadas = 2
                self.limpiar()
                pass
            Mano.__huboParda = False
        elif self.jugador_2.suTurno == True and self.cartas_jugadas[0].jerarquia > self.cartas_jugadas[1].jerarquia:
            self.ganador_mano = self.jugador_2
            self.jugador_2.suTurno = True
            self.jugador_1.suTurno = False
            self.jugador_2.manos_ganadas = self.jugador_2.manos_ganadas + 1
            if self.nro == 1:
                Mano.__ganadorPrimera = self.jugador_2
            if Mano.__huboParda == True and self.nro == 2 or self.nro == 3 :
                self.jugador_2.manos_ganadas = 2
                self.limpiar()
            Mano.__huboParda = False
        elif self.jugador_2.suTurno == False and self.cartas_jugadas[1].jerarquia > self.cartas_jugadas[0].jerarquia:
            self.jugador_2.suTurno = True
            self.jugador_1.suTurno = False
            self.ganador_mano = self.jugador_2
            self.jugador_2.manos_ganadas = self.jugador_2.manos_ganadas + 1
            if self.nro == 1:
                Mano.__ganadorPrimera = self.jugador_2
            if Mano.__huboParda == True and self.nro == 2 or self.nro == 3 :
                self.jugador_2.manos_ganadas = 2
                self.limpiar()
            Mano.__huboParda = False
        else:
            if self.nro == 1:
                Mano.__huboParda = True
                self.ganador_mano = "Hubo parda en primera"
                
            elif self.nro == 2:
                self.ganador_primera()
                if Mano.__ganadorPrimera == None:
                    Mano.__huboParda = True
                    self.ganador_mano = "Hubo parda en segunda"
            elif self.nro == 3:
                if self.jugador_1.manos_ganadas == 1 and self.jugador_2.manos_ganadas == 1 :
                    self.ganador_primera()
                elif self.jugador_1.manos_ganadas == 0 and self.jugador_2.manos_ganadas == 0:
                    if Mano.__es_mano == self.jugador_1:
                        self.ganador_mano = self.jugador_1
                        self.jugador_1.suTurno = True
                        self.jugador_2.suTurno = False
                        self.jugador_1.manos_ganadas = 2
                        self.limpiar()

                    else:
                        self.jugador_2.suTurno = True
                        self.jugador_1.suTurno = False
                        self.ganador_mano = self.jugador_2
                        self.jugador_2.manos_ganadas = 2
                        self.limpiar()

        return self.ganador_mano
    
    def limpiar(self):
        Mano.__prox_nro = 0
        Mano.__es_mano = None
        Mano.__ganadorPrimera = None
        Mano.__huboParda = False   
    def ganador_primera(self):
        if Mano.__ganadorPrimera == self.jugador_1:
            self.ganador_mano = self.jugador_1
            self.jugador_1.suTurno = True
            self.jugador_2.suTurno = False
            self.jugador_1.manos_ganadas = self.jugador_1.manos_ganadas + 1
            self.limpiar()
        else:
            self.jugador_2.suTurno = True
            self.jugador_1.suTurno = False
            self.ganador_mano = self.jugador_2
            self.jugador_2.manos_ganadas = self.jugador_2.manos_ganadas + 1

                  

       