from jugador import Jugador

class RobotIA(Jugador):
    def __init__(self, nombre: str, suTurno: bool = False, ) -> None:
        super().__init__(nombre, suTurno)



    def tirar_carta(self):
        return self.cartas.pop()

    