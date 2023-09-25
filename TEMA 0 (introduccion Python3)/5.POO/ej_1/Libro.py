class Libro:
    def __init__(self, nombre, serial):
        self.nombre = nombre
        self.serial = serial

    def mostrarDatos(self):
        return f"Nombre: {self.nombre}\nNumero serie: {self.serial}"