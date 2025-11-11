from baraja import Baraja
from ma import Ma

class Juego:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.barajar()
        
    def jugar(self):
        majugador = Ma()

        carta = self.baraja.sacar_carta()
        majugador.añadir_Carta(carta)
        majugador.motrar_cartas()
        print("Puntos: ", majugador.valor)

        while majugador.valor < 21:
            accion = input("quieres otra carta? (s/n): ")
            if accion == "s":
                carta = self.baraja.sacar_carta()
                majugador.añadir_Carta(carta)
                majugador.motrar_cartas() 
                print("Puntos: ", majugador.valor)
            else:
                break

        if majugador.valor == 21:
            print("Has ganado, sacaste 21")
        elif majugador.valor > 21:
            print("Has perdido")
        else:
            print("Tu resultado es: ", majugador.valor)