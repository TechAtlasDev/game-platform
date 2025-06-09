import pygame
from utils.evento import Evento
from pygame.surface import Surface
from ..base import PantallaBase

class PantallaJuego(PantallaBase):
  def __init__(self):
    super().__init__()

  def manejar_eventos(self, eventos):
    return super().manejar_eventos(eventos)
  
  def run(self, pantalla:Surface):
    imagen = pygame.image.load("ruta de la imagen")
    pantalla.blit(imagen)