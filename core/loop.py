# Este es un comentario de prueba

import pygame

class Loop:
  def __init__(self):
    self.running = False
  
  def enlistar_eventos(self):
    eventos = pygame.event.get()
    for evento in eventos:
      if evento.type == pygame.QUIT:
        self.running = False
    return eventos
