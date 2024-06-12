from mazo import Mazo
from carta import Carta


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

#ESPADA

# carta1 = Carta('Espada', 1, 14)
# carta6 = Carta('Espada', 7, 12)
# carta2 = Carta('Espada', 3, 10)
# carta10 = Carta('Espada', 2, 9)
# carta9 = Carta('Espada', 12, 7)
# carta8 = Carta('Espada', 11, 6)
# carta7 = Carta('Espada', 10, 5)
# carta5 = Carta('Espada', 6, 3)
# carta4 = Carta('Espada', 5, 2)
# carta3 = Carta('Espada', 4, 1)

# # BASTO

# carta11 = Carta('Basto', 1, 13)
# carta12 = Carta('Basto', 3, 10)
# carta13 = Carta('Basto', 2, 9)
# carta14 = Carta('Basto', 12, 7)
# carta15 = Carta('Basto', 11, 6)
# carta16 = Carta('Basto', 10, 5)
# carta17 = Carta('Basto', 7, 4)
# carta18 = Carta('Basto', 6, 3)
# carta19 = Carta('Basto', 5, 2)
# carta20 = Carta('Basto', 4, 1)

# # COPA

# carta2 = Carta('Copa', 3, 10)
# carta2 = Carta('Copa', 2, 9)
# carta1 = Carta('Copa', 1, 8)
# carta9 = Carta('Copa', 12, 7)
# carta8 = Carta('Copa', 11, 6)
# carta7 = Carta('Copa', 10, 5)
# carta6 = Carta('Copa', 7, 4)
# carta5 = Carta('Copa', 6, 3)
# carta4 = Carta('Copa', 5, 2)
# carta3 = Carta('Copa', 4, 1)

# # ORO

# carta6 = Carta('Oro', 7, 11)
# carta2 = Carta('Oro', 3, 10)
# carta2 = Carta('Oro', 2, 9)
# carta1 = Carta('Oro', 1, 8)
# carta9 = Carta('Oro', 12, 7)
# carta8 = Carta('Oro', 11, 6)
# carta7 = Carta('Oro', 10, 5)
# carta5 = Carta('Oro', 6, 3)
# carta4 = Carta('Oro', 5, 2)
# carta3 = Carta('Oro', 4, 1)



mazo.crear_mazo(mazoGenerico)
# for carta in mazo.cartas:
#     print(carta)

