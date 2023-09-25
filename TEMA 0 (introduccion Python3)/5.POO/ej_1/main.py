from Autor import Autor
from Libro import Libro

def main():
    autor1 = Autor("Elias", "Uruguay")
    libro1 = Libro("Las Aventuras de Peter Parker", 123456)

    print(autor1.mostrarDatos())
    print(libro1.mostrarDatos())

if __name__ == "__main__":
    main()
