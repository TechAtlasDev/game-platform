import pygame

class Boton:
  def __init__(self, texto:str, posicion:tuple[int, int], ancho:int, alto:int):
    self.texto = texto
    self.posicion = posicion
    self.ancho = ancho
    self.alto = alto
    self.fuente_texto = pygame.font.Font(None, 36)

  def renderizar(self, pantalla:pygame.surface.Surface):
    rect = pygame.Rect(self.posicion[0], self.posicion[1], self.ancho, self.alto)
    color = (200, 200, 200)
    pygame.draw.rect(pantalla, color, rect)
    
    border_color = (100, 100, 100)
    pygame.draw.rect(pantalla, border_color, rect, 2)
    
    text = self.fuente_texto.render(self.texto, True, (0, 0, 0))
    pantalla.blit(text, (self.posicion[0] + (self.ancho - text.get_width()) // 2, 
               self.posicion[1] + (self.alto - text.get_height()) // 2))
    
  def al_presionar(self, funcion):
    funcion()