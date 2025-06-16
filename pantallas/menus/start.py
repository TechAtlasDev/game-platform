# -- Tipado de variables
from utils.evento import Evento

# -- Importaciones de pantallas y componentes
from pantallas.componentes.boton import Boton
from pantallas.base import PantallaBase

# Importando el escenario
from pantallas.escenario.main import PantallaJuego

class StartMenu(PantallaBase):
    def __init__(self):
        super().__init__()
        self.color = (100, 100, 200)
        boton = Boton(texto="Jugar", posicion=(100, 100), ancho=200, alto=50)
        self.ventana.add_component(boton)
        boton.al_presionar(
            PantallaJuego, parametros=self.ventana
        )
        
    def manejar_eventos(self, eventos:list[Evento]):
        for evento in eventos:
            if evento.tipo == "click":
                coordenadas = evento.coordenadas

    def run(self):
        self.rellenar_pantalla()

        for componente in self.componentes:
            componente.renderizar(self.ventana)