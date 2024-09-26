#---------

#person
#dni : int
#name : str
#lastname : int
#role : int
#--------------

class Person:
    def __init__(self, dni: int, name: str, lastname: str, role: int):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.role = role

    def __repr__(self):
      return f"{self.dni} {self.name} {self.lastname} {self.role}"

    
person1 = Person(dni=123, name="Luisito", lastname="Velez", role=1)
person2 = Person(dni=1211, name="Lady", lastname="Rodas", role=1)
person3 = Person(dni=2415, name="Julian", lastname="Muñoz", role=1)
person4 = Person(dni=7852, name="Silvana", lastname="Bolaños", role=1)


print(person1)
print(person2)
print(person3)
print(person4)


