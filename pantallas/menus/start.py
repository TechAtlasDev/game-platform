from pygame.surface import Surface
from utils.evento import Evento
from pantallas.componentes.boton import Boton
from pantallas.base import PantallaBase

def ejecutar_escena_1():
    print ("Ejecutando escenario 1")

class StartMenu:
    def __init__(self):
        self.rellenar_pantalla((100,100,100))
        self.boton = Boton("Jugar", (100, 100), 200, 50)
        
    def manejar_eventos(self, eventos:list[Evento]):
        for evento in eventos:
            if evento.tipo == "click":
                coordenadas = evento.coordenadas
                presiono_boton = self.boton.detectar_clic(coordenadas)
                if presiono_boton:
                    self.boton.al_presionar(self.vaciar_pantalla)

    def rellenar_pantalla(self,color):
        self.ventana.fill(color)

    def run(self,ventana:Surface):
        self.ventana=ventana
        self.boton.renderizar(ventana)
    def vaciar_pantalla(self):
        self.rellenar_pantalla((0,0,0))
