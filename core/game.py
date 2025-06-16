from core.ventana import Ventana
from pantallas.menus.start import StartMenu
import pygame
from pygame.surface import Surface
from utils.config import Config
from .loop import Loop

class Game:
  def __init__(self, title:str, config:Config, pantalla:StartMenu):
    self.pantalla = pantalla
    self.title = title
    self.config = config
    self.loop = Loop()
    ventana_pygame:Surface = pygame.display.set_mode((config.width, config.height))
    ventana = Ventana(ventana_pygame)

    self.pantalla.ventana = ventana

  def run(self):
    while self.loop.running:
      eventos = self.loop.enlistar_eventos()
      self.pantalla.manejar_eventos(eventos)
      self.pantalla.run()
      pygame.display.update()
      pygame.time.Clock().tick(self.config.fps)