from mazo import Mazo
from carta import Carta
from ronda import Ronda
from jugador import Jugador
from partida import Partida
from mano import Mano

mazo = Mazo()

palos = ['Basto','Espada', 'Copa', 'Oro']

valores = [1,2,3,4,5,6,7,10,11,12]

mazoGenerico = [
#       ESPADA      
Carta('Espada', 1, 14),
Carta('Espada', 7, 12),
Carta('Espada', 3, 10),
Carta('Espada', 2, 9),
Carta('Espada', 12, 7),
Carta('Espada', 11, 6),
Carta('Espada', 10, 5),
Carta('Espada', 6, 3),
Carta('Espada', 5, 2),
Carta('Espada', 4, 1),
#       BASTO       
Carta('Basto', 1, 13),
Carta('Basto', 3, 10),
Carta('Basto', 2, 9),
Carta('Basto', 12, 7),
Carta('Basto', 11, 6),
Carta('Basto', 10, 5),
Carta('Basto', 7, 4),
Carta('Basto', 6, 3),
Carta('Basto', 5, 2),
Carta('Basto', 4, 1),
#       COPA        
Carta('Copa', 3, 10),
Carta('Copa', 2, 9),
Carta('Copa', 1, 8),
Carta('Copa', 12, 7),
Carta('Copa', 11, 6),
Carta('Copa', 10, 5),
Carta('Copa', 7, 4),
Carta('Copa', 6, 3),
Carta('Copa', 5, 2),
Carta('Copa', 4, 1),
#       ORO     
Carta('Oro', 7, 11),
Carta('Oro', 3, 10),
Carta('Oro', 2, 9),
Carta('Oro', 1, 8),
Carta('Oro', 12, 7),
Carta('Oro', 11, 6),
Carta('Oro', 10, 5),
Carta('Oro', 6, 3),
Carta('Oro', 5, 2),
Carta('Oro', 4, 1)
]

mazo.crear_mazo(mazoGenerico)



# mazo.barajar()
# for carta in mazo.cartas:
#     print(carta)
# print("-" *50)


# for carta in mazo.repartir():
#     print(carta)
# print("-" *50)
# for carta in mazo.cartas:
#     print(carta)

# print("-" *50)


# mazo.reset_mazo()
# for carta in mazo.cartas:
#     print(carta)

# for i in range(16):
#     ronda = Ronda(Mano(Jugador('Francisco', True, True ),Jugador('RobotIA'), ['1 de espada', '1 de copa']))

# jugador1 = Jugador('Francisco', True, True)
jugador2 = Jugador('RobotIA')


# partida = Partida()
# partida.iniciar_ronda(Ronda(Mano(jugador1,jugador2, [Carta('Espada', 7, 12), Carta('Basto', 1, 13) ])))

# print(partida.determinar_ganador())
# print(jugador1.manos_ganadas)
# print(jugador1.rondas_ganadas)
# print("-"*50)
# print(jugador2.manos_ganadas)
# print(jugador2.rondas_ganadas)




