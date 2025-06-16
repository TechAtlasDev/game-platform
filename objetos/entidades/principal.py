import pygame
from pygame.surface import Surface
from .entidad import Entidad


class Heroe(Entidad):
  def __init__(self, coordenadas, ancho=50, alto=50, color=(255, 0, 0), velocidad=1, vida=3):    
    # Atributos específicos del rectángulo
    self.coordenadas = coordenadas
    self.velocidad = velocidad
    self.vida = vida
    self.ancho = ancho
    self.player=pygame.image.load("mariobrasas1zure.png").convert()
    self.alto = alto
    self.activo = True
    self.color = color
    print(f"Rectángulo creado con dimensiones {ancho}x{alto} y color {color}")
  
  def renderizar(self, pantalla:Surface):
  #Renderiza el rectángulo en una pantalla de pygame.  
    if self.esta_vivo():
      # Crear un objeto Rectangulo de pygame
      self.player.set_colorkey((0,0,255))
      
      # Dibujar el rectángulo en la pantalla
      pantalla.blit(self.player,[20,100])
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