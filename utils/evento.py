import pygame
from pygame.event import Event

class Evento:
  def __init__(self):
    self.tipo:str = ""
    self.coordenadas:tuple[int, int] = None

    self.__metadata__ = ""
  
  def _process_(self, data:Event):
    if data.type == pygame.MOUSEBUTTONDOWN:
      self.tipo = "click"
      self.coordenadas = data.pos
    
    elif data.type == pygame.KEYDOWN:
      self.tipo = "tecla"
      self.__metadata__ = pygame.key.name(data.key)
  
  def __eq__(self, value):
    if isinstance(value, str):
      return self.__metadata__.lower() == value.lower()
    return False