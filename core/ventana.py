import pygame

class Ventana:
  def __init__(self, ventana, color=(0, 0, 0)):
    self.vetana:pygame.surface.Surface = ventana
    self.color = color
    self.componentes = []

  def add_component(self, componente):
    self.componentes.append(componente)

  def definir_color(self, color):
    self.color = color