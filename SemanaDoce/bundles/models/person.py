from abc import ABC

#Esta es una clase Abstracta
#Es no instanciable person = Person(...)

class Person(ABC):
    def __init__(self, name, lastname, age, address):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.address = address
