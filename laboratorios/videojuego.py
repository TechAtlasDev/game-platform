import pygame, sys
pygame.init()

#colores
negro =(0,0,0)
blanco =(255,255,255)
verde =(0,255,0)
rojo =(255,0,0)
azul =(0,0,233)
#tamaño de la pantalla
size = (800,500)
#crear
screen = pygame.display.set_mode(size)
#Coords
cord_x = 10
cord_y = 10
#velocidad
speed_x = 3
spee_y  = 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
#color de la pantalla
    screen.fill(rojo)
#dubujo    
    pygame.draw.rect (screen,negro,(cord_x,cord_y,80,80))
    pygame.display.flip()