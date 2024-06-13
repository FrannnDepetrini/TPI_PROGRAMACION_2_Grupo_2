import random
class Generador_cartas():
    
    carta_por_jugador = 3
    cartas_seleccionadas = []
    carta_random = None



    @classmethod
    def generar_carta(cls, mazo):
        for _ in range(0,cls.carta_por_jugador):
            #pop metodo python
            cls.carta_random = random.choice(mazo.cartas)
            cls.cartas_seleccionadas.append(cls.carta_random)
            mazo.remove_cartas(cls.carta_random)
        return cls.cartas_seleccionadas
    

   

