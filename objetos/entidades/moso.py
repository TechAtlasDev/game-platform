import pygame
from .entidad import Entidad

class Mozo(Entidad):
    def __init__(self, coordenadas, ancho=40, alto=80, velocidad=2, vida=5):
        self.coordenadas = coordenadas
        self.activo = True
        self.ancho = ancho
        self.velocidad = velocidad
        self.vida = vida
        self.alto = alto
        self.color = (0, 0, 255)  # Color azul para el mozo
        self.items_llevados = []  # Lista de ítems que lleva el mozo
        self.capacidad_maxima = 3  # Cantidad máxima de ítems que puede llevar
        print(f"Mozo creado con dimensiones {ancho}x{alto}")
    
    def renderizar(self, pantalla):
        """Renderiza el mozo en una pantalla de pygame."""
        if self.esta_vivo():
            # Crear un objeto Rectangulo de pygame para representar al mozo
            rect = pygame.Rect(self.coordenadas[0], self.coordenadas[1], 
                              self.ancho, self.alto)
            
            # Dibujar el mozo en la pantalla
            pygame.draw.rect(pantalla, self.color, rect)
            print(f"Mozo renderizado en {self.coordenadas}")
        else:
            print("No se puede renderizar un mozo inactivo")
    
    def colisiona_con(self, entidad):
        """Verifica la colisión con otra entidad."""
        rect1 = pygame.Rect(self.coordenadas[0], self.coordenadas[1], 
                          self.ancho, self.alto)
        rect2 = pygame.Rect(entidad.coordenadas[0], entidad.coordenadas[1], 
                          entidad.ancho, entidad.alto)
        
        colision = rect1.colliderect(rect2)
        if colision:
            print(f"Mozo colisionó con otra entidad")
        return colision
    
    def recoger_item(self, item):
        
        if len(self.items_llevados) < self.capacidad_maxima:
            self.items_llevados.append(item)
            print(f"Mozo recogió item. Lleva {len(self.items_llevados)} items")
            return True
        else:
            print("El mozo no puede llevar más items")
            return False
    
    def entregar_items(self):
        #Entrega todos los ítems que lleva el mozo.
        items = self.items_llevados.copy()
        self.items_llevados = []
        print(f"Mozo entregó {len(items)} items")
        return items