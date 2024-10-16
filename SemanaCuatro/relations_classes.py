class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book: 'Book'):
        self.books.append(book)

    def get_books(self):
        return f"Libros del autor = {[book.title for book in self.books]}"

#------------------------------------

# class Book:
#     def __init__(self, title: str, pages: int, author: Author):
#         self.title = title
#         self.pages = pages
#         self.Author = author

#     def __str__(self):
#         return f"Libro: {self.title}"


# #------------------------------------

# class Library:
#     def __init__(self):
#         self.books = []




author_1 = Author(name='Gabriel Garcia Marquez')
book_1 = Book('Cien años de soledad', 473, author_1)

author_1.add_books(book_1)


#Llamado atributos de clase

print(author_1.book)


# # #1 crear una lista vacia
# # mi_lista = []
# # print("lista inicial (vacia): ", mi_lista)

# # #2 metodo append() agrega un elemento al final de la lista
# # mi_lista.append(10)
# # mi_lista.append(20)
# # print("\nDespúes de usar append(10) y append(20):", mi_lista)