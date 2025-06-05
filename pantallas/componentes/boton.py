import pygame

class Boton:
  def __init__(self, texto:str, posicion:tuple[int, int], ancho:int, alto:int):
    self.texto = texto
    self.posicion = posicion
    self.ancho = ancho
    self.alto = alto
    self.fuente_texto = pygame.font.Font(None, 36)

  def renderizar(self, pantalla:pygame.surface.Surface):
    self.rectangulo = pygame.Rect(self.posicion[0], self.posicion[1], self.ancho, self.alto)
    color_fondo = (200, 200, 200)
    pygame.draw.rect(pantalla, color_fondo, self.rectangulo)
    
    color_borde = (100, 100, 100)
    pygame.draw.rect(pantalla, color_borde, self.rectangulo, 2)
    
    texto = self.fuente_texto.render(self.texto, True, (0, 0, 0))
    pantalla.blit(texto, (self.posicion[0] + (self.ancho - texto.get_width()) // 2, 
               self.posicion[1] + (self.alto - texto.get_height()) // 2))
    
  def detectar_clic(self, mouse_posicion) -> bool:
    return self.rectangulo.collidepoint(mouse_posicion)
    
  def al_presionar(self, funcion):
    funcion()