from pygame.surface import Surface
from utils.evento import Evento
from pantallas.componentes.boton import Boton

class StartMenu:
    def __init__(self):
        self.boton = Boton("Jugar", (100, 100), 200, 50)
        
    def manejar_eventos(self, eventos:list[Evento]):
        for evento in eventos:
            if evento.tipo == "click":
                coordenadas = evento.coordenadas
                print (f"Click en coordenadas: {coordenadas}")

    def rellenar_pantalla(self, ventana:Surface):
        print ("Rellenando pantalla")
        ventana.fill((100, 250, 100))

    def run(self,ventana:Surface):
        self.rellenar_pantalla(ventana)
        self.boton.renderizar(ventana)
