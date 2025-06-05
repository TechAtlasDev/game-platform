#Creando Figura
import pygame,sys 
pygame.init()
tamaño=(800,600)
negro=(0, 0, 0)
verde=(0, 143, 57)
screen=pygame.display.set_mode(tamaño)
x = 40
y = 40
fps = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            sys.exit()
    #pa presionar
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_d]:
                x += 10
    if teclas[pygame.K_a]:
                x -= 10
    if teclas[pygame.K_w]:
                y -= 10
    if teclas[pygame.K_s]:
                y += 10
    screen.fill(negro)
    rectangulo = pygame.draw.rect(screen, verde, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
    fps.tick(60)


