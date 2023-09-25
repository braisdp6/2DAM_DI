# Mastermind é un xogo que consiste en adiviñar un número.
# Codifica un programa que xenere un número entero aleatorio entre 1 e 100. A continuación iranos pedindo que adiviñemos o número. A axuda do programa será que si erramos diranos que o número que indicamos é maior ou menor que o que número aleatorio. Deberás incluir o número de intentos ao final da execución do programa.
# Ademáis, propoñer o programa para dous xogadores, e quen é o vencedor.
import random

def mastermind():
    numCorrecto = int(random.randrange(1, 101))
    print("Número correcto:", numCorrecto)
    numIntentos = 0

    while True:
        numIntentos += 1
        n = int(input("Adivina un número del 1 al 100: "))
        if n == numCorrecto:
            print("¡Has acertado!\nNúmero de intentos:", numIntentos)
            return numIntentos
        elif n > numCorrecto:
            print("Prueba con un número más bajo.")
        else:
            print("Prueba con un número más alto.")


# Llamada al metodo
print("Jugador 1:")
game1 = mastermind()

print("\nJugador 2:")
game2 = mastermind()

# Resultado
if game1 == game2:
    print("Habeis empatado!")
elif game1 < game2:
    print("El jugador 1 ha ganado.")
else:
    print("El jugador 2 ha ganado.")