from carta import Carta
import random

class Baraja:

    pals = ["Corazones", "Diamantes", "Treboles", "Picas"]
    valores = ["As", "2", "3", "4", "5", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self):
        self.cartas = []
        for pal in self.pals:
            for valor in self.valores:
                cartacreada = Carta(pal, valor)
                self.cartas.append(cartacreada)

    def mostrar(self):
        for carta in self.cartas:
            print(carta)

    def sacar_carta(self):
        return self.cartas.pop()
    
    def barajar(self):
        random.shuffle(self.cartas)
