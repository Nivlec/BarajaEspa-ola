class Ma:
    def __init__ (self):
        self.cartas = []
        self.valor = 0
    
    def añadir_Carta(self, carta):
        self.cartas.append(carta)

        if carta.valor in ["J", "Q", "K"]:
            self.valor += 10
        elif carta.valor == "As":
            self.valor += 11
        else:
            self.valor += int(carta.valor)

    def motrar_cartas(self):
        for carta in self.cartas:
            print(carta)

    
