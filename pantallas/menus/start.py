import pygame
from ..base import PantallaBase
from pantallas.escenario.main import PantallaJuego

class StartMenu(PantallaBase):
  def __init__(self):
    self.texto1 = "Mario Broster" # Creamos una interfaz básica
    self.boton_iniciar = pygame.Rect(100, 100, 200, 50) # El boton para iniciar el juego

  def manejar_eventos(self, eventos):
    for evento in eventos:

      # == CONTROLAR EVENTOS DE TIPO CLICK ==
      if evento.type == pygame.click:
        # == Si el click fue en el boton de iniciar ==
        if self.boton_iniciar.collidepoint(evento.posicion):
          # == Iniciar el juego ==
          pantalla_juego = PantallaJuego()
          pantalla_juego.run()