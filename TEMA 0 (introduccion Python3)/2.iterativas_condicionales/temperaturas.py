# 4. Codificar un programa que nos pida un valor de temperatura é unha
# escala, por exemplo, 273 grados en escala Kelvin e posteriormente
# transforme dita temperatura nas outras escalas coñecidas, neste caso
# sería en Fahrenheit e Graos centígrados Centigrados.
# As fórmulas necesarias son:
# K = 273,1 + ºC
# ºF = 1,4 · ºC + 32


def menu():
    temperatura = float(input("Introduce la temperatura en Grados Centigrados:"))
    opcion = int(input("Elige una opcion:\n(1. Pasar a Kelvin)\n(2. Pasar a Fahrenheith)"))
    if opcion == 1:
        temperatura = transformar_kelvin(temperatura)
        print(temperatura)
    elif opcion == 2:
        temperatura = transformar_fahrenheit(temperatura)
        print(temperatura)
    else:
        print("ERROR")


def transformar_kelvin(temperatura):
    temperatura += 273.1
    return temperatura

def transformar_fahrenheit(temperatura):
    temperatura = 1.4 * temperatura + 32
    return temperatura

menu()