class Rectangulo:
  def __init__(self, coordenadas):
    self.coordenadas = coordenadas # (x, y)

  def mover_izquierda(self):
    self.coordenadas[0] -= 10

  def mover_derecha(self):
    self.coordenadas[0] += 10