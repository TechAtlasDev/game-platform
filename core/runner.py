from core.game import Game
from utils.config import config

#from pantallas.menus.start import StartMenu
from pantallas.escenario.escenario1 import PantallaJuego

game = Game(title="Mario broster", config=config)
pantalla_inicial = PantallaJuego()

def run_game():
  game.run(pantalla_inicial)
