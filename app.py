from datos import *
from generador_carta import *


def loggin():
    name = input("Ingrese su nombre ")
    jugador1 = Jugador(name, True, True)
    return jugador1

jugador1 = loggin()
print(f"Bienvenido al Truco.py {jugador1}|")
while True:
    opt = int(input("1| Jugar al truco\n2| No quiero jugar al truco\nIngrese una opcion: "))
    while opt < 1 and opt > 2:
        opt = int(input("Opcion invalida, solo se admite 1 y 2"))
    if (opt == 1):
        print("...Repartiendo cartas...")

        jugador2.recibir_carta()
        Generador_cartas.limpiar_datos()
        jugador1.recibir_carta()

        while jugador1.rondas_ganadas < 15 and jugador2.rondas_ganadas < 15:
            
            print(jugador1.manos_ganadas)
            print("-"*50)
            print(jugador2.manos_ganadas)


            if (jugador1.suTurno):
                # JUGADOR_HUMANO
                print("Tus cartas son:")
                for i, carta in enumerate(jugador1.cartas, 1):
                    print(f"{i}| {carta}")
                opt_carta = int(input("Cual carta desea tirar? "))

                while opt_carta < 1 or opt_carta > len(jugador1.cartas):
                    print("Numero de opcion invalido, eliga alguna de las disponibles")
                    opt_carta = int(input("Cual carta desea tirar? "))
                    
                cartaTiradaJugador1 = jugador1.cartas[opt_carta-1]
                jugador1.tirar_carta(cartaTiradaJugador1)
                print(f"Tiraste el {cartaTiradaJugador1}")
                
                # JUGADOR_BOT
                cartaTiradaJugador2 = jugador2.tirar_carta_bot()
                print(f"{jugador2} tiro {cartaTiradaJugador2}")
            else:
                # JUGADOR_BOT
                cartaTiradaJugador2 = jugador2.tirar_carta_bot()
                print(f"{jugador2} tiro {cartaTiradaJugador2}")
                # JUGADOR_HUMANO
                print("Tus cartas son:")
                for i, carta in enumerate(jugador1.cartas, 1):
                    print(f"{i}| {carta}")
                opt_carta = int(input("Cual carta desea tirar?"))

                while opt_carta < 1 or opt_carta > len(jugador1.cartas):
                    opt_carta = int(input("Numero de opcion invalido, eliga alguna de las disponibles"))
                    
                cartaTiradaJugador1 = jugador1.cartas[opt_carta-1]
                jugador1.tirar_carta(cartaTiradaJugador1)
                print(f"Tiraste el {cartaTiradaJugador1}")

          
            if (jugador1.suTurno):
                ronda = Ronda(Mano(jugador1,jugador2,[cartaTiradaJugador1, cartaTiradaJugador2]))
                partida1 = Partida()
            else:
                ronda = Ronda(Mano(jugador1,jugador2,[cartaTiradaJugador2, cartaTiradaJugador1]))
                partida1 = Partida()

            print(f"El ganador de la mano fue {ronda.mano.determinar_ganador()}")
            if jugador1.manos_ganadas > 1 or jugador2.manos_ganadas > 1:
                jugador1.cartas.clear()
                jugador2.cartas.clear()
                print(f"El ganador de la ronda fue {ronda.determinar_ganador()}")
                print(f"Yo: {jugador1.rondas_ganadas}\nRobotIA: {jugador2.rondas_ganadas}")
                partida1.iniciar_ronda(ronda)
                jugador1.manos_ganadas = 0
                jugador2.manos_ganadas = 0
                mazo.barajar()
                jugador2.recibir_carta()
                Generador_cartas.limpiar_datos()
                jugador1.recibir_carta()
        print(f"El ganador de la partida ha sido {partida1.determinar_ganador()}")    
            

    else:   # SI ELIGE OPCION 2 (SALIR)
        print("Gracias por jugar al Truco.py")
        break