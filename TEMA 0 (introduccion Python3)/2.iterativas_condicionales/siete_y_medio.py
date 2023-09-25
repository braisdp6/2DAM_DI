# 5. Codifica un programa que simule unha partida ao 7 e medio coa
# baralla española entre dous xogadores. Para elo o programa
# sacara para cada xogador un número aleatorio entre 1 e 10 tendo
# en conta que o 8, 9 e 10 simularán a sota, cabalo e rei,
# respectivamente que no xogo do 7 e medio valen medio punto.
# Cada xogador pódese plantar cando queira e gañará o que máis
# se aproxime por debaixo ao 7 e medio.
# Por exemplo:
# O xogador A saca o 4 e 2 e a sota (8) ten 6 e medio e plántase.
# O xogador B saca o 4 e 5 e xa perde porque pasou de 7 e medio.
# Gaña o xogador A.
# Cada partida finalizada pregunta se queremos seguir ou deixar o
# xogo.

import random


def main():
    total_jugador1 = 0
    total_jugador2 = 0
    salir = False
    # Juega el primer jugador
    print("JUGADOR 1:")
    while not salir:
        total_jugador1 += sacar_carta()
        print("Total puntos: ", total_jugador1)
        if total_jugador1 > 7.5:
            print("El JUGADOR 1 ha perdido.")
            salir = True
        else:
            salir = seguir_jugando()

    # Juega el segundo jugador
    print("JUGADOR 2:")
    salir = False
    while not salir:
        total_jugador2 += sacar_carta()
        print("Total puntos: ", total_jugador2)
        if total_jugador2 > 7.5:
            print("El JUGADOR 2 ha perdido.")
            salir = True
        else:
            salir = seguir_jugando()

    # Comparacion para ver ganador
    total_jugador1 -= 7.5
    total_jugador2 -= 7.5
    if total_jugador1 == total_jugador2:
        print("¡Empate!")
    elif total_jugador1 > total_jugador2:
        print("El JUGADOR 1 ha ganado.")
    else:
        print("El JUGADOR 2 ha ganado.")


def sacar_carta():
    ultima_carta = random.randint(1, 10)
    print("Has sacado un", ultima_carta)
    if ultima_carta > 7:
        ultima_carta = 0.5
    return ultima_carta


def seguir_jugando():
    comprobador_menu = False
    salir = False
    while not comprobador_menu:
        opcion = int(input("¿Deseas seguir jugando?\n(1. Seguir jugando)\n(0. Salir)"))
        if opcion == 0:
            salir = True
            comprobador_menu = True
        elif opcion == 1:
            comprobador_menu = True
        else:
            print("Opcion no válida.")
    return salir


main()
