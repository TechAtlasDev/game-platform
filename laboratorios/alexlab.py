import pygame
import random
import pygame.font
import pygame.event

from pygame.surface import Surface
class Color:
    def __init__(self, r:int, g:int, b:int):
        self.r = r
        self.g = g
        self.b = b
class AlexLab:
    def __init__(self, title:str):
        self.title = title
        pygame.init()
        pygame.display.set_caption(self.title)
        self.ventana:Surface = pygame.display.set_mode((800, 600))
    def run(self):
        running = True
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False
            r = random.randint(0, 255);g = random.randint(0, 255);b = random.randint(0, 255)
            self.ventana.fill((0, 0, 0))
            font_inicio = pygame.font.Font(None, 36)
            texto_inicio = font_inicio.render("Iniciar", 0, (0, 0, 0))
            self.ventana.blit(texto_inicio, (100, 100))
            boton_inicio = pygame.Rect(80, 100, 200, 50)
            pygame.draw.rect(self.ventana, (r, g, b), boton_inicio)#colores aleatorios 
            blit = self.ventana.blit(texto_inicio, (boton_inicio.x + 50, boton_inicio.y + 10))
            pygame.draw.rect(self.ventana, (255, 255, 255), boton_inicio, 2)

            if boton_inicio.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    print("Botón Iniciar presionado")
            pygame.display.update()






GAME = AlexLab("Alex Lab")

GAME.run()

