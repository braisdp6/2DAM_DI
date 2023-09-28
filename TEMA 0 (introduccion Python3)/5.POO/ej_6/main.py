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

    accion = input("¿Qué deseas hacer? (atacar/huir): ").lower()
    if accion == "atacar":
        personaje.atacar(enemigo)
    if enemigo.esta_vivo():
        enemigo.atacar(personaje)
    elif accion == "huir":
    print("Escapas del combate.")
    break

    else:
    print("Acción no válida. Ingresa 'atacar' o 'huir'.")
    if enemigo.vida <= 0:
        experiencia_ganada = random.randint(10, 20)
    personaje.ganar_experiencia(experiencia_ganada)
    print(f"Has derrotado al {enemigo.nombre} enemigo y ganado {experiencia_ganada} puntos de experiencia.")
    else:
    print("Has sido derrotado por el {enemigo.nombre} enemigo.")
    print("\nEl juego ha terminado.")
    if personaje.experiencia >= 50:
        print(f"{personaje.nombre} ha ganado el juego y se ha convertido en un gran guerrero.")


if __name__ == "__main__":
    main()
