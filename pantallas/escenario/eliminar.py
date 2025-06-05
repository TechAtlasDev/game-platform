from pantallas.base import PantallaBase

class Escenario(PantallaBase):
  def __init__(self):
    print ("Escenario ha sido creado")

  def manejar_eventos(self, eventos):
    print ("Manejando eventos en el escenario")

  def rellenar_pantalla(self, ventana):
    print ("Rellenando pantalla del escenario")
  
  def run(self, ventana):
    print ("Ejecutando escenario")