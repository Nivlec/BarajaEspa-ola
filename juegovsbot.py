from baraja import Baraja
from ma import Ma

class Juegovsbot:
    def __init__(self):
        self.baraja = Baraja()
        self.baraja.barajar()
        
    def jugar(self):
        majugador = Ma()
        mabot = Ma()

                    #Mi mano
        print("     Mis cartas")
        carta = self.baraja.sacar_carta()
        majugador.añadir_Carta(carta)
        majugador.motrar_cartas()
        print("             Puntos: ", majugador.valor)

                    #Mano del bot
        print("     Cartas del bot")
        carta = self.baraja.sacar_carta()
        mabot.añadir_Carta(carta)
        mabot.motrar_cartas()
        print("             Puntos: ", mabot.valor)

        while majugador.valor < 21 or mabot.valor < 21:
            print("                     Tu turno")
            accion = input("quieres otra carta? (s/n): ")
            if accion == "s":
                carta = self.baraja.sacar_carta()
                majugador.añadir_Carta(carta)
                majugador.motrar_cartas() 
                print("         Puntos: ", majugador.valor)
                
                print("                 Turno bot")
                carta = self.baraja.sacar_carta()
                mabot.añadir_Carta(carta)
                mabot.motrar_cartas()
                print("         Puntos bot: ", mabot.valor)
            
            elif accion == "n":
                print("                 Turno bot")
                carta = self.baraja.sacar_carta()
                mabot.añadir_Carta(carta)
                mabot.motrar_cartas()
                print("         Puntos bot: ", mabot.valor)
            else:
                break
            if majugador.valor == 21:
                print("        Has ganado, sacaste 21")
                break
            elif mabot.valor == 21:
                print("         Te gano un bot, lol")
                break
            elif majugador.valor > 21:
                print("         Has perdido")
                break
            elif mabot.valor > 21:
                print("         El bot perdió, tú ganas")
                break
            else:
                print("         Tu resultado es: ", majugador.valor)
                print("         Resultado del bot: ", mabot.valor)
       
                

       