import pygame
from utils.evento import Evento
from pygame.surface import Surface
from ..base import PantallaBase
from objetos.entidades.moso import Mozo
from objetos.entidades.rectangulo import Rectangulo

class PantallaJuego(PantallaBase):
  def __init__(self):
    self.imagen=pygame.image.load("fondo.png").convert()
    self.rectangulo = Rectangulo(coordenadas=[100, 100], velocidad=10)
    self.mozo1 = Mozo(coordenadas=[0, 0],ancho=40,alto=80,velocidad=1,vida=5)

  def manejar_eventos(self, eventos):
    for evento in eventos:
      if evento.tipo == "tecla":
        if evento == "w":
          self.rectangulo.mover_arriba()
        elif evento=="s":
          self.rectangulo.mover_abajo()
        elif evento=="d":
          self.rectangulo.mover_derecha()
        elif evento=="a":
          self.rectangulo.mover_izquierda()

        
  
  def run(self, pantalla:Surface):
    pantalla.blit(self.imagen,[0,0])
    self.rectangulo.renderizar(pantalla)
    self.mozo1.mover_izquierda()
    self.mozo1.renderizar(pantalla)
