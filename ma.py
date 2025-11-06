class Ma:
    def __init__ (self):
        self.cartas = []
    
    def añadir_Carta(self, carta):
        self.cartas.append(carta)

    def motrar_cartas(self):
        for carta in self.cartas:
            print(carta)