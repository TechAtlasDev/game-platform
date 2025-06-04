from pygame.surface import Surface
import pygame

class StartMenu:
    def __init__(self):
        pass
    def manejar_eventos(self, eventos):
        self.pos=pygame.mouse.get_pos()
        print(self.pos[0],self.pos[1])

    def rellenar_pantalla(self, ventana:Surface):
        ventana.fill((255, 255, 255))

    def run(self,ventana:Surface):
        self.rellenar_pantalla(ventana)