import pygame 

pygame.init()


screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("primer personaje")
image1 = pygame.image.load("personajes/mario_brasas1.png")
image2 = pygame.image.load("personajes/mario_brasas2.png")  
image3 = pygame.image.load("personajes/mario_brasas3.png")
image4 = pygame.image.load("personajes/mario_brasas4.png")
image5 = pygame.image.load("personajes/mario_brasas5.png")
image6 = pygame.image.load("personajes/mario_brasas6.png")
image7 = pygame.image.load("personajes/mario_brasas7.png")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(image1, (70, 100))
    screen.blit(image2, (200, 100))
    screen.blit(image3, (300, 100))
    screen.blit(image4, (400, 100))
    screen.blit(image5, (500, 100))
    screen.blit(image6, (600, 100))
    screen.blit(image7, (700, 100))
    pygame.display.flip()
    pygame.time.delay(100)  # retraso entre imagenes
    screen.fill((0, 0, 0))  # limpiar la pantalla 
pygame.quit() 
