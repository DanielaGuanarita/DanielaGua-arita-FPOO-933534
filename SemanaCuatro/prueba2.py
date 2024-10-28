# Diccionario de especialidades

Especialidades = {
1: "Cardiología",
2: "Neurología",
3: "Pediatría",
4: "Ginecología",
5: "Medico General"
}


class Paciente:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'{self.nombre}, {self.edad} años'



class Doctor:
    def __init__(self, nombre, especialidad_num):
        self.nombre = nombre
        self.especialidad = Especialidades.get(especialidad_num, 'Especialidad desconocida')
        self.citas = []  


    def agregar_cita(self, paciente, fecha, hora):
        self.citas.append((paciente, fecha, hora))


    def mostrar_citas(self):
            print(f'Dr. {self.nombre}, Especialidad: {self.especialidad}')
            for cita in self.citas:
                paciente, dia, hora = cita
                print(f'Cita el dia {dia}, a las {hora}, con {paciente}')
        

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = [] 
        self.pacientes = [] # Lista para almacenar doctores


    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def agregar_pacientes(self, paciente):
        self.pacientes.append(paciente)

    # Método para mostrar las citas
    def mostrar_doctores_y_citas(self):
        for doctor in self.doctores:
            doctor.mostrar_citas()


    # Método para mostrar solo las citas de los doctores
    def mostrar_solo_citas(self):
        for doctor in self.doctores:
            for cita in doctor.citas:
                paciente, dia, hora = cita
                print(f'Cita el dia {dia}, a las {hora}, con {paciente}')

    
    # Método para mostrar solo los nombres de los doctores
    def mostrar_doctores(self):
        print("Listado de Doctores:")
        for doctor in self.doctores:
            print(f'Dr./Dra. {doctor.nombre}, Especialidad: {doctor.especialidad}')
    



hospital = Hospital("Clínica Sebastian de Belalcazar")


doctor1 = Doctor("Alejandro Ortiz", 1)
doctor2 = Doctor("Ana Maria Rojas", 3)
doctor3 = Doctor("Maria Alejandra Ramirez", 2)
doctor4 = Doctor("Jacobo Goméz", 4)
doctor5 = Doctor("Adrian Garcia", 5)

# Agregar doctores al hospital
hospital.agregar_doctor(doctor1)
hospital.agregar_doctor(doctor2)
hospital.agregar_doctor(doctor3)
hospital.agregar_doctor(doctor4)
hospital.agregar_doctor(doctor5)


# Crear pacientes
paciente1 = Paciente("Emma Ramirez", 12)
paciente2 = Paciente("Lucia Rojas", 31)
paciente3 = Paciente("Felipe Estrada", 27)
paciente4 = Paciente("Camila Reyes", 19)
paciente5 = Paciente("Juan David Zuluaga", 26)

# Agregar citas a los doctores
doctor1.agregar_cita(paciente1, "24-10-2024", "10:00 AM")
doctor3.agregar_cita(paciente2, "28/10/2024", "02:45 PM")
doctor2.agregar_cita(paciente1, "01/11/2024", "06:20 PM")
doctor4.agregar_cita(paciente3, "12/11/2024", "03:40 PM")
doctor5.agregar_cita(paciente5, "15/11/2024", "01:15 PM")
doctor1.agregar_cita(paciente4, "23/11/2024", "09:00 AM")
doctor3.agregar_cita(paciente5, "13/12/2024", "07:30 AM")

# # Mostrar doctores y sus citas
hospital.mostrar_doctores_y_citas()

# Método para mostrar solo las citas de un doctor específico
# doctor1.mostrar_citas()

# Mostrar solo las citas de todos los doctores
# hospital.mostrar_solo_citas()

# Mostrar solo el listado de doctores
# hospital.mostrar_doctores()



# class Director:
#     def __init__(self, name, nacionality, movies):
#         self.name = name
#         self.nacionality = nacionality
#         self.movies = []


#     def __str__(self):
#         return f"{self.name}"

#     def add_movie(self, movie):
#         self.movies.append(movie)

#     def get_movies(self):
#         return self.movies


# class Movies:
#     def __init__(self, title, generate, duration, director):
#         self.title = title
#         self.generate = generate
#         self.duration = duration
#         self.director = director

#     def __repr__(self):
#         return f"Movies(title={self.title}, generate={self.generate}, duration={self.duration}, director={self.director})"
     


# class Cinema: 
#     def __init__(self, name, address, bilboard):     
#         self.name = name
#         self.address = address
#         self.bilboard = bilboard
#         self.movies = []
    



#     def add_movie(self, movie):
#         self.movies.append(movie)

#     def get_movies(self):
#         return self.movies


# def main():

#     director_1 = Director('M. Night Shyamalan', 'India', [])
#     director_2 = Director('Dennis Dugan', 'Estadounidense', [])
#     director_3 = Director('Matthew Vaughn', 'Londres', [])


#     movie_1 = Movies('Fragmentado', 'Terror intriga', 1.57,  director_1)
#     movie_2 = Movies('Los huespedes', 'Terror', 1.34, director_1)
#     movie_3 = Movies('Una esposa de mentiras', 'Comedia-Romance', 1.57, director_2)
#     movie_4 = Movies('Son como niños dos', 'Comedia', 1.41, director_2)
#     movie_5 = Movies('Kingsman', 'Accion', 2.09, director_3)



#     cinema_1 = Cinema('Cine colombia', 'Cra 49 # 9-5o', 'Fragmentado')
#     cinema_2 = Cinema('Royal films', 'Cra 98 # 16-200', 'Los huespedes')
#     cinema_3 = Cinema('Cinepolis', 'Clle 5 # 69-03', 'Una esposa de mentiras')



#     director_1.add_movie(movie_1)
#     director_1.add_movie(movie_2)
#     director_2.add_movie(movie_3)
#     director_2.add_movie(movie_4)
#     director_3.add_movie(movie_5)



#     cinema_1.add_movie(movie_1)
#     cinema_1.add_movie(movie_2)
#     cinema_2.add_movie(movie_3)
#     cinema_2.add_movie(movie_4)
#     cinema_3.add_movie(movie_5)

#     for movie in cinema_2.movies:
#         print(cinema_1)




#     # list_movies = cinema.get_movies()

#     # for movie in list_movies:
#     #     print(movie.director)


# main()