import random


class Enemigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(50, 100)
        self.ataque = random.randint(5, 15)
        self.defensa = random.randint(3, 10)

    def esta_vivo(self):
        # si la vida es mayor que cero
        if self.vida<=0:
            return False
        else:
            return True
        
    def atacar(self, personaje):
        #variable danio es el resultado de ataque menos defensa
        danho=self.ataque-personaje.defensa
        if danho > 0:
            #al enemigo le restamos vidas
            personaje.vida-=danho
            print(f"{self.nombre} ataca a {personaje.nombre} y le causa {danho} puntos de daño.")
            personaje.mostrarVida()
        else:
            print(f"{self.nombre} ataca a {personaje.nombre}, pero no causa daño.")
            personaje.mostrarVida()
        
    def mostrar_estado(self):
        print(f"{self.nombre}: Vida = {self.vida}, Ataque = {self.ataque}, Defensa = {self.defensa}")
        

class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 10
        self.defensa = 5
        self.experiencia = 0

    def atacar(self, enemigo):
        #variable danio es el resultado de ataque menos defensa
        danho=self.ataque-enemigo.defensa
        if danho > 0:
            #al enemigo le restamos vidas
            enemigo.vida-=danho
            print(f"{self.nombre} ataca a {enemigo.nombre} y le causa {danho} puntos de daño.")

        else:
            print(f"{self.nombre} ataca a {enemigo.nombre}, pero no causa daño.")

    def ganar_experiencia(self, experiencia_ganada):
        #suma experiencia
        self.vida+=20
        self.experiencia+=experiencia_ganada
        print(f"{self.nombre} ha ganado {experiencia_ganada} puntos de experiencia.")

    def esta_vivo(self):
        #si la vida es mayor que cero
        if self.vida<=0:
            return False
        else:
            return True

    def mostrar_estado(self):
        print(f"{self.nombre}: Vida = {self.vida}, Ataque = {self.ataque}, Defensa = {self.defensa}, Experiencia = {self.experiencia}")

    def mostrarVida(self):
        print(f"Tienes {self.vida} puntos de vida.")



def main():
    nombre_personaje = input("Ingresa el nombre de tu personaje: ")
    personaje = Personaje(nombre_personaje)
    enemigos = [Enemigo("Orco"), Enemigo("Shawk"), Enemigo("Drago")]
    while personaje.esta_vivo():
        enemigo = random.choice(enemigos)
        print(f"\nTe encuentras con un {enemigo.nombre} enemigo.")
        while enemigo.esta_vivo() and personaje.esta_vivo():
            print("\nEstado actual:")
            personaje.mostrar_estado()
            enemigo.mostrar_estado()
            accion = int(input("¿Qué deseas hacer? 1->Atacar//2->Huir: "))
            if accion == 1:
                probabilidad=random.randint(1,100)
                if probabilidad>70:
                    personaje.atacar(enemigo) 
                else:
                    print("Has fallado el ataque")
                if enemigo.esta_vivo():
                        probabilidad2=random.randint(1,100)
                        if probabilidad2>70:
                            enemigo.atacar(personaje)
                        else:
                            print("Ha fallado el ataque")
            elif accion == 2:
                probabilidad=random.randint(1,100)
                if probabilidad>50:
                    print("No has sido capaz de escapar")
                    enemigo.atacar(personaje)
                else:
                    print("Escapas del combate.")
                    break
            else:
                print("Acción no válida. Ingresa 'atacar' o 'huir'.")
        if enemigo.vida <= 0:
            experiencia_ganada = random.randint(10, 20)
            personaje.ganar_experiencia(experiencia_ganada)
            enemigo.vida=random.randint(50, 100)
            print(f"Has derrotado al {enemigo.nombre} enemigo y ganado {experiencia_ganada} puntos de experiencia.")
        else:
            print(f"Has sido derrotado por el {enemigo.nombre} enemigo.")
            
        if personaje.experiencia >= 50:
            print(f"{personaje.nombre} ha ganado el juego y se ha convertido en un gran guerrero.")
            print("\nEl juego ha terminado.")
            break

if __name__ == "__main__":
    main()