import pygame
from entidad import Entidad

class Rectangulo(Entidad):
  def __init__(self, coordenadas, ancho=50, alto=50, color=(255, 0, 0), velocidad=1, vida=3):    
    # Atributos específicos del rectángulo
    self.ancho = ancho
    self.alto = alto
    self.color = color
    print(f"Rectángulo creado con dimensiones {ancho}x{alto} y color {color}")
  
  def renderizar(self, pantalla):
  #Renderiza el rectángulo en una pantalla de pygame.  
    if self.esta_vivo():
      # Crear un objeto Rectangulo de pygame
      rect = pygame.Rect(self.coordenadas[0], self.coordenadas[1], 
                self.ancho, self.alto)
      
      # Dibujar el rectángulo en la pantalla
      pygame.draw.rect(pantalla, self.color, rect)
      print(f"Rectángulo renderizado en {self.coordenadas}")
    else:
      print("No se puede renderizar un rectángulo inactivo")
  
  def colisiona_con(self, entidad):
    #Verificamos la colisión con un True si es que la hay o con un False caso contrario
    #Crear Rectangulos de pygame para la detección de colisiones
    rect1 = pygame.Rect(self.coordenadas[0], self.coordenadas[1], 
               self.ancho, self.alto)
    rect2 = pygame.Rect(entidad.coordenadas[0], entidad.coordenadas[1], 
               entidad.ancho, entidad.alto)
    
    colision = rect1.colliderect(rect2)
    if colision: # -> True o False
      print(f"Colisión detectada con otra entidad")
    else:
      print(f"No hay colisión con otra entidad")
    return colision