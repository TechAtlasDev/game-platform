from utils.config import Config
from .loop import Loop

class Game:
  def __init__(self, title:str, config:Config):
    self.title = title
    self.config = config
    self.loop = Loop()

  def run(self, pantalla):
    while self.loop.running:
      eventos = self.loop.enlistar_eventos()
      pantalla.run(eventos)
