from pantallas.menus.start import StartMenu
import pygame
from pygame.surface import Surface
from utils.config import Config
from .loop import Loop

class Game:
  def __init__(self, title:str, config:Config):
    self.title = title
    self.config = config
    self.loop = Loop()
    self.ventana:Surface = pygame.display.set_mode((config.width, config.height))

  def run(self, pantalla:StartMenu):
    while self.loop.running:
      eventos = self.loop.enlistar_eventos()
      pantalla.manejar_eventos(eventos)
      pantalla.run(self.ventana)
      pygame.display.update()