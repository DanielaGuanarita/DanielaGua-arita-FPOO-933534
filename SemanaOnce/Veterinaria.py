class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.__nombre = nombre
        self.__tipo = tipo
        self.edad = edad

    def __str__(self):
            return f"{self.__nombre}, Tipo de mascota: {self.__tipo}, Edad:{self.edad}"

class Dueno:
    def __init__(self, nombre, telefono, mascota):
        self.__nombre = nombre
        self.__telefono = telefono
        self.mascotas = []

    def get_nombre(self):
        return self.__nombre

    def get_telefono(self):
        return self.__telefono

    def agregar_mascota(self, mascota):
            self.mascotas.append(mascota)

    def __str__(self):
        mascotas_info =""
        for mascota in self.mascotas:
            mascotas_info+= str(mascota) + "\n"
        return f"Dueño: {self.__nombre}, \n Telefono: {self.__telefono}, \n Mascota: {self.mascotas_info.strip}"

        

class Consulta:
    def __init__(self, fecha, motivo, mascota, dueno, telefono):
        self.fecha = fecha
        self.motivo = motivo
        self.mascota = mascota
        self.dueno = dueno
        self.telefono = telefono


    def __str__(self):
        return f" Fecha consulta: {self.fecha},\n Motivo de consulta: {self.motivo}, \n Mascota: {self.mascota},\n Dueño: {self.dueno}, Telefono:{self.telefono}"
    
mascota1 = Mascota('Cosmo', 'Gato', '2 años')
mascota2 = Mascota('Apolo', 'Gato', '1 año')

dueno1 = Dueno('Daniela Guañarita', '3153389830', 'Gato')

dueno1.agregar_mascota(mascota1)
dueno1.agregar_mascota(mascota2)

consulta1= Consulta('15 de noviembre', 'vacunacion', mascota1, dueno1.get_nombre(), dueno1.get_telefono())

print(consulta1)

