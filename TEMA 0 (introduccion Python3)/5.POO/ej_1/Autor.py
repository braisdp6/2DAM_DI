class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def mostrarDatos(self):
        return f"Nombre: {self.nombre}\nNacionalidad: {self.nacionalidad}"