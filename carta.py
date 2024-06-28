

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
        self.__palo = new_palo

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, new_valor):
        self.__valor = new_valor

    @property
    def jerarquia(self):
        return self.__jerarquia
    
    @jerarquia.setter
    def jerarquia(self, new_jerarquia):
        self.__jerarquia = new_jerarquia
        


    def __str__(self) -> str:
        return f"{self.valor} de {self.palo}"