from core.game import Game
from utils.config import config

from pantallas.menus.start import StartMenu

game = Game(title="Mario broster", config=config)
pantalla_inicial = StartMenu()

def run_game():
  game.run(pantalla_inicial)
