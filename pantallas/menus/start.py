from pygame.surface import Surface
from utils.evento import Evento

class StartMenu:
    def __init__(self):
        pass
        
    def manejar_eventos(self, eventos:list[Evento]):
        for evento in eventos:
            if evento.tipo == "click":
                coordenadas = evento.coordenadas
                print (f"Click en coordenadas: {coordenadas}")

    def rellenar_pantalla(self, ventana:Surface):
        ventana.fill((100, 255, 100))

    def run(self,ventana:Surface):
        self.rellenar_pantalla(ventana)


