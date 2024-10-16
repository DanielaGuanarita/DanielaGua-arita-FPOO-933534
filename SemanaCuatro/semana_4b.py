# class Author:
#     def __init__(self, name, books):
#         self.name = name
#         self.books = []


#     def __str__(self):
#         return f"{self.name}"

#     def add_book(self, book):
#         self.books.append(book)

#     def get_books(self):
#         return self.books


# class Book:
#     def __init__(self, title, pages, author):
#         self.title = title
#         self.pages = pages
#         self.author = author

#     def __repr__(self):
#         return f"Book(title={self.title}, pages={self.pages}, author={self.author})"

# class Library: 
#     def __init__(self, ):
#         self.books = []
    
#     def add_book(self, book):
#         self.books.append(book)

#     def get_books(self):
#         return self.books



# def main():

#     author_1 = Author('Gabriel', [])
#     author_2 = Author('Neruda', [])

#     book_1 = Book('Cien años de soledad', 493, author_1)
#     book_2 = Book('El coronel no tiene quien le escriba', 703, author_1)
#     book_3 = Book('La felicidad', 293, author_2)

#     # print(author_1)

#     author_1.add_book(book_1)
#     author_1.add_book(book_2)
#     author_2.add_book(book_3)

#     books_author2 =author_2.get_books()

#     library = Library()

#     library.add_book(book_1)
#     library.add_book(book_2)
#     library.add_book(book_3)


#     list_books = library.get_books()

#     for book in list_books:
#         print(book.author)

# main()





# # for book in books_author1:
# #     print(book)


# # #print(author_1)


class Director:
    def __init__(self, name, nacionality, movies):
        self.name = name
        self.nacionality = nacionality
        self.movies = []


    def __str__(self):
        return f"{self.name}"

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movies(self):
        return self.movies


class Movies:
    def __init__(self, title, generate, duration, director):
        self.title = title
        self.generate = generate
        self.duration = duration
        self.director = director

    def __repr__(self):
        return f"Movies(title={self.title}, generate={self.generate}, duration={self.duration}, director={self.director})"
     


class Cinema: 
    def __init__(self, name, address, bilboard):     
        self.name = name
        self.address = address
        self.bilboard = bilboard
        self.movies = []
    



    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movies(self):
        return self.movies


def main():

    director_1 = Director('M. Night Shyamalan', 'India', [])
    director_2 = Director('Dennis Dugan', 'Estadounidense', [])
    director_3 = Director('Matthew Vaughn', 'Londres', [])


    movie_1 = Movies('Fragmentado', 'Terror intriga', 1.57,  director_1)
    movie_2 = Movies('Los huespedes', 'Terror', 1.34, director_1)
    movie_3 = Movies('Una esposa de mentiras', 'Comedia-Romance', 1.57, director_2)
    movie_4 = Movies('Son como niños dos', 'Comedia', 1.41, director_2)
    movie_5 = Movies('Kingsman', 'Accion', 2.09, director_3)



    cinema_1 = Cinema('Cine colombia', 'Cra 49 # 9-5o', 'Fragmentado')
    cinema_2 = Cinema('Royal films', 'Cra 98 # 16-200', 'Los huespedes')
    cinema_3 = Cinema('Cinepolis', 'Clle 5 # 69-03', 'Una esposa de mentiras')



    director_1.add_movie(movie_1)
    director_1.add_movie(movie_2)
    director_2.add_movie(movie_3)
    director_2.add_movie(movie_4)
    director_3.add_movie(movie_5)



    cinema_1.add_movie(movie_1)
    cinema_1.add_movie(movie_2)
    cinema_2.add_movie(movie_3)
    cinema_2.add_movie(movie_4)
    cinema_3.add_movie(movie_5)

    for movie in cinema_2.movies:
        print(cinema_1)




    # list_movies = cinema.get_movies()

    # for movie in list_movies:
    #     print(movie.director)


main()