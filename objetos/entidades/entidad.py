class Entidad:
  def __init__(self, coordenadas, velocidad=1, vida=3):
    """
    Inicializa una entidad con coordenadas, velocidad y vida.
    """
    self.coordenadas = coordenadas
    self.velocidad = velocidad
    self.vida = vida
    self.activo = True
    print(f"Entidad creada en {self.coordenadas} con velocidad {self.velocidad} y vida {self.vida}")
  
  def mover_izquierda(self):
    """Mueve la entidad hacia la izquierda."""
    self.coordenadas[0] -= self.velocidad
    print(f"Moviendo izquierda. Nueva posición: {self.coordenadas}")
  
  def mover_derecha(self):
    """Mueve la entidad hacia la derecha."""
    self.coordenadas[0] += self.velocidad
    print(f"Moviendo derecha. Nueva posición: {self.coordenadas}")
  
  def mover_arriba(self):
    """Mueve la entidad hacia arriba."""
    self.coordenadas[1] -= self.velocidad
    print(f"Moviendo arriba. Nueva posición: {self.coordenadas}")
  
  def mover_abajo(self):
    """Mueve la entidad hacia abajo."""
    self.coordenadas[1] += self.velocidad
    print(f"Moviendo abajo. Nueva posición: {self.coordenadas}")
  
  def dañar(self, unidades):
    """
    Reduce la vida de la entidad según las unidades de daño.
    """
    self.vida -= unidades
    print(f"Dañado por {unidades} unidades. Vida restante: {self.vida}")
    
    if self.vida <= 0:
      self.morir()
  
  def curar(self, unidades):
    """
    Aumenta la vida de la entidad según las unidades de curación.
    """
    self.vida += unidades
    print(f"Curado por {unidades} unidades. Vida actual: {self.vida}")
  
  def cambiar_velocidad(self, nueva_velocidad):
    """
    Cambia la velocidad de la entidad.
    """
    self.velocidad = nueva_velocidad
    print(f"Velocidad actualizada a: {self.velocidad}")
  
  def morir(self):
    """Gestiona la muerte de la entidad."""
    self.activo = False
    print(f"Entidad en {self.coordenadas} ha muerto")
  
  def esta_vivo(self):
    """Verifica si la entidad está viva."""
    return self.activo