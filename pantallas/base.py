from pygame.surface import Surface
from utils.evento import Evento

class PantallaBase:
  def __init__(self):
    pass

  def manejar_eventos(self, eventos:list[Evento]):
    """
    Maneja los eventos de entrada del usuario.
    :param eventos: Lista de eventos de pygame.
    """
    for evento in eventos:
      if evento.tipo == "click":
        if evento == "w":
          print ("Se presionó W")

  def run(self, pantalla:Surface):
    """
    Ejecuta la lógica de la pantalla.
    :param pantalla: Superficie de pygame donde se renderiza la pantalla.
    """
    self.ventana = pantalla
    self.rellenar_pantalla((100, 100, 100))

  def rellenar_pantalla(self,color):
      self.ventana.fill(color)

  def vaciar_pantalla(self):
      self.rellenar_pantalla((0,0,0))

