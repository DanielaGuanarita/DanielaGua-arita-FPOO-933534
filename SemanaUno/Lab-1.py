class Contacto:
    def __init__(self, nombre, apellido, organizacion, telefono, direccion):
        self.datos = [nombre, apellido, organizacion, telefono, direccion]

    def obtener_datos(self):
        return self.datos


class Directorio:
    def __init__(self):
        self.contactos = [["Nombre", "Apellido", "Organización", "Teléfono", "Dirección"]]

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto.obtener_datos())
    
    def mostrar_contactos(self):
        # Muestra el directorio en formato tabular
        print("Contact Directory:\n")
       
        for fila in self.contactos:
            print("| {:<15} | {:<10} | {:<15} | {:<15} | {:<28} |".format(*fila))


directorio = Directorio()

directorio.agregar_contacto(Contacto("Ana Maria", "Rojas", "Banco Union", "3155455580", "Calle 54 B 23, Ciudad Cali"))
directorio.agregar_contacto(Contacto("Maria Camila", "Carmona", "Davivienda", "3197624571", "Cra 23 12 48, Ciudad Cali"))
directorio.agregar_contacto(Contacto("Juan Camilo", "Ramirez", "Bancolombia", "3204159652", "Calle 48 9 52, Ciudad Cali"))


directorio.mostrar_contactos()
