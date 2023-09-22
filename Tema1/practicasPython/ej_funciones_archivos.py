import random
# Ejercicios PYTHON: Funciones

# EJERCICIO Nº1:
# Codifica un programa “Loterías” que conteña un
# menú que acceda as seguintes funcións:
# 1. Un xerador de apostas da primitiva (6 números entre 1 e 49
# máis o complementario entre 1 e o 9).
# 2. Xerador de Euromillóns (5 números entre 1 e 50 máis dous
# números “estrela” entre 1 e 12).
# 3. Un xerador de apostas da quiniela de fútbol, 15 resultados
# entre 1,X,2.
# 4. Un xerador de Lotería nacional. Un número entre o 00000 e o
# 99999.
# Valorarase que o menú sexa outra función.

def main():
    loteria()

def loteria ():
    combinacion_num = []
    num_complementario = []
    opcion = menu()
    if opcion is 1:
        combinacion_num = random.sample(range(1, 50), 6)
        num_complementario = random.randint(1, 9)
    elif opcion is 2:
        combinacion_num = random.sample(range(1, 51), 5)
        num_complementario = random.sample(range(1, 13), 2)
    elif opcion is 3:
        combinacion_num = random.sample(range(1, 3), 15)
        num_complementario = random.sample(range(1, 13), 2)
        print(combinacion_num)



def menu():
    while True:
        opcion = int(input("Introduce un numero:\n(1. Primitiva)\n(2. Euromillones)\n(3. Quiniela futbol)\n(4. Loteria nacional)"))
        if opcion >= 1 and opcion <= 4:
            break
    return opcion

# Ejecutador
main()