from pygame.surface import Surface

class StartMenu:
    def __init__(self):
        pass
    def manejar_eventos(self, eventos):
        print("manejando eventos")

    def rellenar_pantalla(self, ventana):
        ventana.fill((255, 255, 255))

    def run(self,ventana:Surface):
        self.rellenar_pantalla(ventana)
        print("Alejandro no trabaja")