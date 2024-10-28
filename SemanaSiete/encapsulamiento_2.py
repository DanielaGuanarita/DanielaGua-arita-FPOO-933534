class Vehiculo:
    def __init__(self, velocidad):
        self.__velocidad = velocidad

    def acelerar(self, valor):
        if valor > 0:
            self.__velocidad += valor
            
    
    def freno(self, valor):
        if valor > 0:
            self.__velocidad -= valor
            if self.__velocidad < 0:
                self.__velocidad = 0

    def __str__(self):
        return f'Su velocidad es: {self.__velocidad}'

vehiculo1 = Vehiculo(15)
print(vehiculo1)

vehiculo1.freno(5)
print(vehiculo1)

vehiculo1.acelerar(5)
print(vehiculo1)