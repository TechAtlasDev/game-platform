from pygame.surface import Surface
from utils.evento import Evento
import pygame

class StartMenu:
    def __init__(self):
        pass
    def manejar_eventos(self, eventos:list[Evento]):
        for evento in eventos:
            if evento.tipo == "click":
                coordenadas = evento.coordenadas
            elif evento.tipo == "tecla":
                if evento == "q":
                    pass


    def rellenar_pantalla(self, ventana:Surface):
        ventana.fill((255, 255, 255))

    def run(self,ventana:Surface):
        self.rellenar_pantalla(ventana)