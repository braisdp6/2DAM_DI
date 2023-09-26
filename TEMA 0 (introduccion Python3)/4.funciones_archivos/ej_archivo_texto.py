def crear_archivo():
    nombre_archivo = input("Introduce el nombre del archivo .txt a crear: ")
    archivo = open(nombre_archivo, "w")
    archivo.close()
    print("Archivo creado exitosamente.")

def escribir_texto():
    nombre_archivo = input("Introduce el nombre del archivo .txt: ")
    texto = input("Introduce el texto a guardar: ")
    archivo = open(nombre_archivo, "a")
    archivo.write(texto + "\n")
    archivo.close()
    print("Texto guardado exitosamente.")

def contar_vocales():
    nombre_archivo = input("Introduce el nombre del archivo .txt: ")
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()
    archivo.close()

    vocales = 0
    for caracter in contenido:
        if caracter.lower() in "aeiouáéíóú":
            vocales += 1

    print("Contenido del archivo:")
    print(contenido)
    print("Número de vocales:", vocales)

def agregar_frase():
    nombre_archivo = input("Introduce el nombre del archivo .txt: ")
    frase = input("Introduce la frase a agregar: ")
    archivo = open(nombre_archivo, "a")
    archivo.write(frase + "\n")
    archivo.close()
    print("Frase agregada exitosamente.")

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear archivo")
        print("2. Escribir texto")
        print("3. Contar vocales")
        print("4. Agregar frase")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            escribir_texto()
        elif opcion == "3":
            contar_vocales()
        elif opcion == "4":
            agregar_frase()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()