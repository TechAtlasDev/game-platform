from pygame.surface import Surface
from core.ventana import Ventana
from utils.evento import Evento

class PantallaBase:
  def __init__(self):
    self.ventana:Ventana
    self.componentes = []
    self.color = (100, 100, 100)

  def manejar_eventos(self, eventos:list[Evento]):
    """
    Maneja los eventos recibidos.
    Este método debe ser implementado por las subclases.
    """
    raise NotImplementedError("Este método debe ser implementado por las subclases.")    
  
  def rellenar_pantalla(self, color=None):
    """
    Rellena la pantalla con un color específico.
    :param color: Color a usar para rellenar. Si es None, se usa self.color.
    """
    if color:
      self.ventana.fill(color)
    else:
      self.ventana.fill(self.color)
  
  def run(self):
    """
    Ejecuta la lógica de la pantalla.
    Este método debe ser implementado por las subclases.
    """
    raise NotImplementedError("Este método debe ser implementado por las subclases.")
  
  def vaciar_pantalla(self):
    """
    Limpia la pantalla.
    Este método puede ser llamado por las subclases para vaciar la pantalla.
    """
    self.color = (0, 0, 0)
    self.rellenar_pantalla()
