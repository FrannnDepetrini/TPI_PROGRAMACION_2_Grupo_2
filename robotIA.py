from jugador import Jugador

class RobotIA(Jugador):
    def __init__(self, nombre: str, puntos: int = 0, suTurno: bool = False, esJugador: bool = False) -> None:
        super().__init__(nombre, puntos, suTurno, esJugador)



    def tirar_carta(self):
        return self.cartas.pop()

    