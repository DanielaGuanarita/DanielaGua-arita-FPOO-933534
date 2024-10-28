class Person:
    def __init__(self, name, age, genero, cedula):
        self._name = name
        self._age = age
        self._genero = genero
        self.__cedula = cedula



    #Metodos de accesibilidad (getters y setters)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_genero(self):
        return self._genero

    def set_genero(self, new_genero):
        self._genero = new_genero
    
#--------------------------------

person1 = Person('Juan', 18, 'Masculino', 114235)

# print(person1._name, person1._age)

print(person1.get_name (), person1.get_age(), person1.get_genero(), person1.__cedula)
person1.set_age(19)
person1.set_genero('Femenino')
person1.set_name('Lucia')
print(person1.get_name (), person1.get_age(), person1.get_genero(), person1.__cedula)