from core.game import Game
from utils.config import config

from pantallas.menus.start import StartMenu

pantalla_inicial = StartMenu()
game = Game(title="Mario broster", config=config, pantalla=pantalla_inicial)

def run_game():
  game.run()
