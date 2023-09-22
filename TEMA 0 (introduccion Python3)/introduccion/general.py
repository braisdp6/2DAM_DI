# 4. Escribir un programa que lle pida ao usuario seu peso (en kg) e estatura
# (en metros), calcule o índice de masa corporal e o almacene nunha variable mostrando por
# pantalla a frase: Teu índice de masa corporal é  <imc >, con dos decimales.
# Fórmula: imc = peso/estatura2

peso = float(input("Introduce tu peso en (kg)"))
estatura = float(input("Introduce tu altura (metros)"))
indiceMasaCorporal = (peso / (estatura * estatura))
print(round(indiceMasaCorporal, 2))

# 5. Escribe un programa que solicite la fecha de nacimiento de un usuario y calcule su edad actual.
import datetime

fechaNacimiento = input("Ingresa tu fecha de nacimiento (YYYY-MM-DD):")
# 2000-10-02
fechaNacimiento = datetime.datetime.strptime(fechaNacimiento, "%Y-%m-%d")
# print("- ",fechaNacimiento)

fechaActual = datetime.datetime.now()
# print("- ",fechaActual)
diferenciaFechas = (fechaActual - fechaNacimiento)
# print("- ",diferenciaFechas)
edadUsuario = int(diferenciaFechas.days / 365)
# print("- ", edadUsuario)

print("Tu edad es: ", edadUsuario, " años.")

# 6. Dado el radio de una circunferencia calcula su perímetro y área.
# Usad función math para usar pi
import math

radio = float(input("Introduce radio:"))

print("Perimetro: ", (2 * math.pi * radio))
print("Area: ", (math.pi * (radio * radio)))
