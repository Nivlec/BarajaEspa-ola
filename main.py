from ma import Ma
from carta import Carta
from baraja import Baraja

baraja = Baraja()
baraja.barajar()
ma = Ma()

carta_sacada = baraja.sacar_carta()
ma.añadir_Carta(carta_sacada)

ma.motrar_cartas()
print("valor de la mano: ", ma.valor)

