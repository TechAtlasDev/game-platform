# Importa tu pantalla, por ejemplo:
from pantallas.menus.start import StartMenu

from utils.config import config
from core.game import Game

juego = Game(
  title="Verificador de Pantallas",
  config=config
)

# Inicia tu pantalla
pantalla = StartMenu()

juego.run(
  pantalla=pantalla
)