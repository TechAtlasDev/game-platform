from pygame.surface import Surface
from utils.evento import Evento
from pantallas.componentes.boton import Boton
from menus.start import StartMenu
from utils.evento import Evento

def ejecutar_escena_1():
    print ("Ejecutando escenario 1")

class RestartMenu(StartMenu):
    def __init__(self):
        self.boton = Boton("Reiniciar", (100, 100), 200, 50)

    def manejar_eventos(self, eventos:list[Evento]):
        super().manejar_eventos(self,eventos)
    def rellenar_pantalla(self, ventana:Surface):
        ventana.fill((10, 250, 10))

    def run(self,ventana:Surface):
        self.rellenar_pantalla(ventana)
        self.boton.renderizar(ventana)