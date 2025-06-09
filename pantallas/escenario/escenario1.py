import pygame
from utils.evento import Evento
from pygame.surface import Surface
from ..base import PantallaBase


class PantallaJuego(PantallaBase):
  def __init__(self):
    self.imagen=pygame.image.load("fondo.png").convert()

  def manejar_eventos(self, eventos):
    return super().manejar_eventos(eventos)
  
  def run(self, pantalla:Surface):
    pantalla.blit(self.imagen,[0,0])
