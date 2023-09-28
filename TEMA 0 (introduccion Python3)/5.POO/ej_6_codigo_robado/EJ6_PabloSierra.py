import random
class Personaje:
    def __init__ (self,nombre):
        self.nombre = nombre
        self.HP = 100
        self.DMG = 10
        self.DEF = 5
        self.XP = 0
    def atacar(self,enemigo):
        #DMG-DEF
        Damages = self.DMG - enemigo.DEF
        if Damages > 0:
            enemigo.HP -= Damages 
            
            #RESTAR DMG A LA VIDA
            print(f"{self.nombre} atacar a {enemigo.nombre} y le causa la perdida de {Damages} HP" )
        else:
            print(f"{self.nombre} ataca a {enemigo.nombre}, pero no causa DMG")
    def ganar_experiencia(self,cantidad):
        self.XP += cantidad
        #Sumar XP
        print(f"{self.nombre} ganó {cantidad} de XP")
    def esta_vivo(self):
        if self.HP > 0:
            return True
            
        else:
            return False
        #HP < 0
    def mostrar_estado(self):
        print(f"{self.nombre}: HP = {self.HP}, DMG = {self.DMG}, DEF = {self.DEF}, XP = {self.XP}")
class Enemigo:
    def __init__ (self, nombre):
        self.nombre = nombre
        self.HP = random.randint(5,10)
        self.DMG = random.randint(5,15)
        self.DEF = random.randint(3,10)
    def atacar(self, personaje):
        Damages = self.DMG - personaje.DEF
        if Damages > 0:
            personaje.HP -= Damages
        
            print(f"{self.nombre} ataca a {personaje.nombre} y le causa la perdida de {Damages}  HP")
        else:
            print(f"{self.nombre} ataca a {personaje.nombre}, pero no caussa DMG")
    def mostrar_estado(self):
        print(f"{self.nombre}: HP = {self.HP}, DMG = {self.DMG}, DEF = {self.DEF}")
    def esta_vivo(self):
        if self.HP > 0:
            return True
        else:
            return False
        #HP < 0
def main():
    nombre_personaje = input("Ingresa el nombre de tu personaje: ")
    personaje = Personaje(nombre_personaje)
    while personaje.esta_vivo():
        enemigos = [Enemigo("Orco"), Enemigo("Shawk"), Enemigo("Drago")]
        enemigo = random.choice(enemigos)
        print(f"\nTe encuentras con un {enemigo.nombre} enemigo.")
        while enemigo.esta_vivo() and personaje.esta_vivo():
            print("\nEstado actual:")
            personaje.mostrar_estado()
            enemigo.mostrar_estado()
            accion = input("¿Qué deseas hacer? (atacar/escapar): ").lower()
            if accion == "atacar":
                personaje.atacar(enemigo)
                if enemigo.esta_vivo():
                    enemigo.atacar(personaje)
            elif accion == "escapar":
                
                print("Escapas del combate.")
                break
            else:
                print("Acción no válida. Ingresa 'atacar' o 'escapar'.")
        if enemigo.HP <= 0:
            experiencia_ganada = random.randint(10, 20)
            personaje.ganar_experiencia(experiencia_ganada)
            print(f"Has derrotado al {enemigo.nombre} enemigo y ganado {experiencia_ganada} puntos de experiencia.")
            
        if personaje.HP <=0:
            print(f"Has sido derrotado por el {enemigo.nombre} enemigo.")
            print("\nEl juego ha terminado.")
            
        if personaje.XP >= 50:
            print(f"{personaje.nombre} ha ganado el juego y se ha convertido en un gran guerrero.")
            input() 
            
       
if __name__ == "__main__":
    main()