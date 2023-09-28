class Agenda:
    def __init__(self):
        self.lista_contactos = []

    def agregar_contacto(self, contacto):
        with open("datos.txt", "a") as archivo:
            for i in contacto:
                archivo.write(str(i) + " ")
            archivo.write("\n")

    def eliminar_contacto(self, telefono):
        with open("datos.txt", "r") as archivo:
            lineas = archivo.readlines()

        with open("datos.txt", "w") as archivo:
            for linea in lineas:
                datos = linea.strip().split()
                if datos[2] != str(telefono):
                    archivo.write(linea)

    def buscar_contacto(self, telefono):
        with open("datos.txt", "r") as archivo:
            lineas = archivo.readlines()

        for linea in lineas:
            datos = linea.strip().split()
            if datos[2] == str(telefono):
                print(datos)


def main():
    salir = False
    while not salir:
        aux = int(input("Elige una opcion:\n(1. Agregar contacto)\n(2. Eliminar contacto)\n(3. Buscar contacto)\n(0. Salir)"))
        if aux == 1:
            agenda = Agenda()
            nombre = input("Introduce el nombre:")
            agenda.lista_contactos.append(nombre)

            correo = input("Introduce el correo:")
            agenda.lista_contactos.append(correo)

            telefono = input("Introduce el telefono:")
            agenda.lista_contactos.append(telefono)
            nuevo = agenda.lista_contactos

            agenda.agregar_contacto(nuevo)

        elif aux == 2:
            agenda = Agenda()
            telefono = int(input("Introduce el telefono:"))
            agenda.eliminar_contacto(telefono)

        elif aux == 3:
            agenda = Agenda()
            telefono = int(input("Introduce el telefono:"))
            agenda.buscar_contacto(telefono)

        elif aux == 0:
            salir = True
        else:
            print("ERROR, saliendo del programa...")


if __name__ == "__main__":
    main()
