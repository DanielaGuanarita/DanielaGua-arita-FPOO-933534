class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.libros = []


    def __str__(self):
        return f"({self.nombre}, {self.nacionalidad})"

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        return self.libros


class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __repr__(self):
        return f"({self.titulo}, de {self.autor})"


class Secciones:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = [] 

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
            print(f'Sección: {self.nombre}')
            for libro in self.libros:
                print(f' {libro}')


    def mostrar_libros_de_autor(autor):
        list = []
        for libro in self.libros:
            if libro.autor == autor:
                list.append(libro.titulo)

        print(list)



def main():

    autor_1 = Autor('Gabriel Garcia Marquez', 'Colombiano')
    autor_2 = Autor('Stephen King', 'Estadounidense')
    autor_3 = Autor("J.K. Rowling", 'Reino Unido')

    libro_1 = Libro('Cien años de soledad', autor_1)
    libro_2 = Libro('El instituto', autor_2)
    libro_3 = Libro('El cazador de sueños', autor_2)
    libro_4 = Libro('Harry Potter y la piedra filosofal', autor_3)

    seccion_ficcion = Secciones("Ficción")
    seccion_fantasia = Secciones("Fantasía")
    seccion_terror = Secciones("Terror")


    seccion_ficcion.agregar_libro(libro_1)
    seccion_terror.agregar_libro(libro_2)
    seccion_terror.agregar_libro(libro_3)
    seccion_fantasia.agregar_libro(libro_4)


main()
