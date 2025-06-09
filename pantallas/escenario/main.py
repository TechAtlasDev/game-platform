from utils.evento import Evento
from pygame.surface import Surface
from ..base import PantallaBase


class PantallaJuego(PantallaBase):
  def __init__(self):
    pass


  def manejar_eventos(self, eventos):
    return super().manejar_eventos(eventos)
  
  def run(self, pantalla):
    self.ventana=pantalla
    self.rellenar_pantalla((0,204,214))
  