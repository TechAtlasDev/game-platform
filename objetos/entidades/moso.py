class Moso:
    def __init__(self , nombre , nivel , posicion):
        self.nombre = nombre
        self.nivel = nivel
        self.posicion = posicion
        self.vida = 100
    def mover_derecha(self, pasos=1):
        self.posicion[0] += pasos
    def mostrar_posicion(self):
        print(f"{self.nombre}) esta en la posicion {self.posicion}")

moso = Moso("Mozo",0,[0,0])
moso.mostrar_posicion()
moso.mover_derecha()
moso.mostrar_posicion()