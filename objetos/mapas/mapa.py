from ..estructuras.estructura import Estructura
from ..entidades.entidad import Personaje

class Mapa:
  def __init__(self):
    self.entidades:list[Personaje] = []
    self.estructuras:list[Estructura] = []

  def agregar_entidad(self, entidad: Personaje):
    self.entidades.append(entidad)