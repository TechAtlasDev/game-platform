from pantallas.escenario.main import Escenario 
from loop import bucle1,buble2 
from personaje import Personaje 
import pygame 
 
class Pantallas_principal: 
    def init(self,config): 
        self.config=config 
    def evento_cerrar(self,eventos): 
        for eventos in eventos: 
            if eventos.type ==pygame.QUIT: 
                bucle1.correr=False 
                 
    def pasar_ventana(self): 
        bucle1.correr=False 
        bucle2.correr=True 
        |