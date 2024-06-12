from datos import *
import random
from mazo import Mazo
from ronda import Ronda

class Generador_cartas():
    
    carta_por_jugador = 3
    mazo_cartas_seleccionadas = []
    carta_random = None
    mazo_generico = mazo.cartas



    @classmethod
    def generar_carta(cls):
        for _ in range(0,cls.carta_por_jugador):
            #pop metodo python
            cls.carta_random = random.choice(mazo.cartas)
            cls.mazo_cartas_seleccionadas.append(cls.carta_random)
            mazo.remove_cartas(cls.carta_random)
        return cls.mazo_cartas_seleccionadas
    

   

# generador = Generador_cartas()

# cartas = []
# cartas.append(generador.generar_carta())

# for carta in mazo.cartas:
#     print(carta)
# print("-" *50)
# for carta in cartas:
#     for x in carta:
#         print(x)
# mazo.reset_mazo()
# print("-" *50)
# for carta in mazo.cartas:
#     print(carta)
