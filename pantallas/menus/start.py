from pygame.surface import Surface
from utils.evento import Evento
from pantallas.componentes.boton import Boton

from pantallas.base import PantallaBase

from pantallas.escenario import Escena1

def ejecutar_escena_1():
    escena = Escena1()
    escena.run()    

class StartMenu(PantallaBase):
    def __init__(self):
        self.boton = Boton("Jugar", (100, 100), 200, 50)
        
    def manejar_eventos(self, eventos:list[Evento]):
        for evento in eventos:
            if evento.tipo == "click":
                coordenadas = evento.coordenadas
                presiono_boton = self.boton.detectar_clic(coordenadas)
                if presiono_boton:
                    self.boton.al_presionar(funcion=ejecutar_escena_1)

    def rellenar_pantalla(self, ventana:Surface):
        ventana.fill((100, 250, 100))

    def run(self,ventana:Surface):
        self.rellenar_pantalla(ventana)
        self.boton.renderizar(ventana)
