def clasificar_categoria(numero):
    categorias = {
        1: "Quiz",
        2: "Parcial",
        3: "Trabajo"
    }
    return categorias.get(numero)

def registrar_tareas():
    tareas = [] 

    while True:
        print("\n Registro de Tareas Académicas ")
        id_tarea = input("Ingrese el ID de la tarea: ")
        titulo = input("Ingrese el título de la tarea: ")
        
        while True:
            try:
                calificacion = float(input("Ingrese la calificación (de 0 a 5): "))
                if 0 <= calificacion <= 5:
                    break
                else:
                    print("Por favor, ingrese una calificación entre 0 y 5.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        while True:
            try:
                categoria = int(input("Ingrese la categoría (1 = Quiz, 2 = Parcial, 3 = Trabajo): "))
                if categoria in [1, 2, 3]:
                    break
                else:
                    print("Por favor, ingrese una categoría válida (1, 2 o 3).")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        
        descripcion_categoria = clasificar_categoria(categoria)

        tarea = {
            'ID': id_tarea,
            'Título': titulo,
            'Calificación': calificacion,
            'Categoría': descripcion_categoria
        }
        tareas.append(tarea)

        seguir = input("¿Desea registrar otra tarea? (s/n): ").lower()
        if seguir != 's':
            break
    return tareas

def imprimir_tareas(tareas):
    print("\n  Listado de Tareas Académicas  ")
    for tarea in tareas:
        print(f"ID: {tarea['ID']}, Título: {tarea['Título']}, Calificación: {tarea['Calificación']}, Categoría: {tarea['Categoría']}")

def resumen_de_tareas():
    tareas = registrar_tareas() 
    imprimir_tareas(tareas) 

resumen_de_tareas()