

class Carta():
    def __init__(self, palo:str, valor:int,jerarquia:int):
        self.__palo= palo
        self.__valor= valor
        self.__jerarquia= jerarquia

    @property
    def palo(self):
        return self.__palo
    
    @palo.setter
    def palo(self, new_palo):
        self.palo = new_palo

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, new_valor):
        self.valor = new_valor

    @property
    def jerarquia(self):
        return self.__jerarquia
    
    @jerarquia.setter
    def jerarquia(self, new_jerarquia):
        self.jerarquia = new_jerarquia
        


    def __str__(self) -> str:
        return f"La carta es el {self.valor} de {self.palo} [{self.jerarquia}]"