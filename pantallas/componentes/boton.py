import pygame
import pygame.font

class Boton:
  def __init__(self, texto:str, posicion:tuple[int, int], ancho:int, alto:int):
    self.texto = texto
    self.posicion = posicion
    self.ancho = ancho
    self.alto = alto

    if not pygame.font.get_init():
        pygame.font.init()
    self.content = pygame.font.Font(None, 36)

  def renderizar(self, pantalla):
    text = self.content.render(self.texto, True, (0, 0, 0))
    pantalla.blit(text, (self.posicion[0] + (self.ancho - text.get_width()) // 2, 
                         self.posicion[1] + (self.alto - text.get_height()) // 2))