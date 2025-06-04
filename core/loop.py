import pygame
from utils.evento import Evento

class Loop:
  def __init__(self):
    self.running = True
  
  def enlistar_eventos(self) -> list[Evento]:
    eventos = pygame.event.get()
    for evento in eventos:
      if evento.type == pygame.QUIT:
        self.running = False
    return eventos