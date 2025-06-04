import pygame,sys

pygame.init()
tamaño=(800,600)
clock=pygame.time.Clock()
color=(150,150,250)
verde=(250,250,250)
screen=pygame.display.set_mode(tamaño)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill(color)
    pygame.display.flip()