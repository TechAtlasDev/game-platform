import pygame
from ..base import PantallaBase
from objetos.entidades import Jugador
from objetos.mapas.mapa import Mundo1

class PantallaJuego(PantallaBase):
  def __init__(self):
    self.mundo = Mundo1()
    self.jugador = Jugador()

  def manejar_eventos(self, eventos):
    for evento in eventos:
      # == CONTROLAR EVENTOS DE TIPO TECLADO ==
      if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT:
          self.jugador.mover_izquierda()
        elif evento.key == pygame.K_RIGHT:
          self.jugador.mover_derecha()
        elif evento.key == pygame.K_UP:
          self.jugador.saltar()
      
  def run(self):
    self.mundo.add(self.jugador) # Agregar el jugador al mundo
    self.mundo.run() # Ejecutar el mundo