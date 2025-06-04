# Este es un comentario
import pygame
from utils.evento import Evento

class Loop:
  def __init__(self):
    self.running = True
  
  def enlistar_eventos(self) -> list[Evento]:
    eventos_procesados = []
    eventos = pygame.event.get()
    for evento in eventos:
      if evento.type == pygame.QUIT:
        self.running = False

      else:
        evento_procesado = Evento()
        evento_procesado._process_(evento)
        eventos_procesados.append(evento_procesado)
        
    return eventos_procesados