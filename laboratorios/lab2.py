import pygame

# Preparate porque vamos a crear un juego
pygame.init()

dimensiones_pantalla = (600, 600)

color_fondo_pantalla = (135, 206, 235) 
# Vamo a crear la pantalla
pantalla = pygame.display.set_mode(dimensiones_pantalla) # Establecer las dimensiones de la pantalla
# Establecer el titulo de la ventana
pygame.display.set_caption("Mario bross pirata")


coordenadas_personaje_x = 150
coordenadas_personaje_y = 150
ancho_personaje = 30
alto_personaje = 60

correr_juego = True

while correr_juego:
  print ("¡Hola, mundo!")
  correr_juego = False