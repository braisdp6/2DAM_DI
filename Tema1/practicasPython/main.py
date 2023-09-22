import random
from collections import Counter

# Pedir al usuario la cantidad de elementos que desea en la lista
n = int(input("Ingrese la cantidad de elementos en la lista: "))

# Crear una lista de N elementos con números aleatorios entre 1 y 10
lista = [random.randint(1, 10) for _ in range(n)]

# Mostrar la lista
print("Lista generada:", lista)

# Calcular el número que más se repite en la lista
conteo = Counter(lista)
numero_mas_comun = max(conteo, key=conteo.get)
repeticiones = conteo[numero_mas_comun]

# Mostrar el número que más se repite y cuántas veces
print(f"El número que más se repite es {numero_mas_comun} y aparece {repeticiones} veces.")
