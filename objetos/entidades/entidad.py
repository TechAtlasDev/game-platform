class Personaje:
    def init(self, vida, nombre, habilidades):
        self.nombre = nombre
        self.vidas = vida
        self.habilidad = habilidades
    def mostrar_habilidades(self):
        return f"{self.nombre} tiene las siguentes hablidades para atacar {self.habilidad}"
    def Salud_actual(self, enemigo):
        self.enemigo = 10
        x = f"{self.nombre} recibio un ataque de {enemigo}"
        
        if x == True:
            self.enemigo-=5
            print(f"{self.nombre} perdio 5 {self.enemigo}")

        else:
            print(f"{self.nombre} no esquivo el ataque.")
    def ataque_personaje(self):
        x= f"{self.nombre} realizo un ataque con su habilidad {self.habilidad}"
        if x == True:
            print(f"{self.nombre} Elimino al villano.")
        else:
            print(f"El {self.enemigo} esquivo el ataque de {self.nombre}")
mario_bross = Personaje("mario bros" ,0 [0,0])
mario_bross.mostrar_habilidades()
mario_bross.Salud_actual()
mario_bross.