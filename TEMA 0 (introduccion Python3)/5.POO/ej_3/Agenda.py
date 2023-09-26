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
                if datos[2] != telefono:
                    archivo.write(linea)


def main():
    salir = False
    while not salir:
        agenda = Agenda()
        nombre = input("Dame el nombre:")
        agenda.lista_contactos.append(nombre)

        correo = input("Dame el correo:")
        agenda.lista_contactos.append(correo)

        telefono = input("Dame el telefono:")
        agenda.lista_contactos.append(telefono)
        nuevo = agenda.lista_contactos

        agenda.agregar_contacto(nuevo)
        # Salida bucle
        aux = int(input("Deseas crear otro contacto?\n(1. Si)\n(0. Salir)"))
        if aux == 1:
            salir = False
        elif aux == 0:
            salir = True
        else:
            print("ERROR, saliendo del programa...")


if __name__ == "__main__":
    main()
