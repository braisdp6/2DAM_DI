# 1. A conxetura de Collatz indica que calquera número natural pode transformarse en 1 aplicando os pasos seguintes: si é par, dividir por 2, se é impar multiplicar por 3 e sumarlle 1.
# Codifica un programa que pedindo un número mostre toda a sucesión de números resultantes ata convertilo en 1.

num = int(input("Introduce un numero:"))
while num > 1:
    if num % 2 != 0:
        print("Numero impar: ", num)
        num = (num * 3) + 1
    else:
        print("Numero par: ", num)
        num = num / 2
print("\nNumero final: ", num)