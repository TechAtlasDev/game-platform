class Principal:
    def __init__(self , nombre , nivel , posicion):
        self.nombre = nombre
        self.nivel = nivel
        self.posicion = posicion
        self.vida = 100
    def mover_derecha(self, pasos=1):
        self.posicion[0] += pasos
    def mostrar_posicion(self):
        print(f"{self.nombre}) esta en la posicion {self.posicion}")

mario_broster = Principal("mario_broster",0,[0,0])
mario_broster.mostrar_posicion()
mario_broster.mover_derecha()
mario_broster.mostrar_posicion()