from datos import *
from generador_carta import *


def loggin():
    name = input("Ingrese su nombre ")
    jugador1 = Jugador(name, True, True)
    return jugador1


def turnoJugador1():

    lista_turno_jugador1 = []

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

    lista_turno_jugador1.append(cartaTiradaJugador1)
    lista_turno_jugador1.append(cartaTiradaJugador2)

    return lista_turno_jugador1

def turnoJugador2():
    
    lista_turno_jugador2 = []
    
    # JUGADOR_BOT
    cartaTiradaJugador2 = jugador2.tirar_carta_bot()
    print(f"{jugador2} tiro {cartaTiradaJugador2}")
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

    lista_turno_jugador2.append(cartaTiradaJugador2)
    lista_turno_jugador2.append(cartaTiradaJugador1)

    return lista_turno_jugador2
    





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

        partida1 = Partida()

        while jugador1.rondas_ganadas < 15 and jugador2.rondas_ganadas < 15:


            if (jugador1.suTurno): 
                lista_turno_jugador1 = turnoJugador1()
            else: 
                lista_turno_jugador2 = turnoJugador2()



            if (jugador1.suTurno):
                ronda = Ronda(Mano(jugador1,jugador2,lista_turno_jugador1))
            else:
                ronda = Ronda(Mano(jugador1,jugador2,lista_turno_jugador2))

            
            ronda.mano.determinar_ganador() # Determina el ganador de la mano
            print(f"Mano {ronda.mano.es_mano}")
            print(f"Primera {ronda.mano.ganador_primera}")
            print("\n")
            if jugador1.manos_ganadas > 1 or jugador2.manos_ganadas > 1:

                jugador1.cartas.clear()
                jugador2.cartas.clear()

                print(f"El ganador de la ronda fue {ronda.determinar_ganador()}")
                print(f"Yo: {jugador1.rondas_ganadas}")
                print("-"*50)
                print(f"RobotIA: {jugador2.rondas_ganadas}")

                if (ronda.mano.es_mano == jugador1.nombre):
                    jugador1.suTurno = False
                    jugador2.suTurno = True
                else:
                    jugador1.suTurno = True
                    jugador2.suTurno = False

                partida1.iniciar_ronda(ronda)
                jugador1.manos_ganadas = 0
                jugador2.manos_ganadas = 0
                mazo.barajar()
                jugador2.recibir_carta()
                Generador_cartas.limpiar_datos()
                jugador1.recibir_carta()


        print(f"El ganador de la partida ha sido {partida1.determinar_ganador()}")
        jugador1.rondas_ganadas = 0
        jugador2.rondas_ganadas = 0
        jugador1.cartas.clear()
        jugador2.cartas.clear()
        opt_ver_resumen = int(input("1| Ver resumen\n2| Salir\nIngrese una opcion: "))

        if opt_ver_resumen == 1:
            for i, ronda in enumerate(partida1.rondas, 1):
                print(f"{i}| {ronda.determinar_ganador()}")

    else:   # SI ELIGE OPCION 2 (SALIR)
        print("Gracias por jugar al Truco.py")
        break