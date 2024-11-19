while True:

    number_1 = input('Por favor ingrese un número: ')
    number_2 = input('Por favor ingrese otro número: ')

    try:
        resultado = int(number_1) / int(number_2)
        print(f'El resultado es: {resultado}')

    except Exception as e:
        print(F'Se produjo un error del tipo: {e}')


    # try:
    #     resultado = int(number_1) / int(number_2)
    #     print(f'El resultado es: {resultado}')
    # except ValueError:
    #     print("ERROR: Por favor ingrese solo números")
    # except ZeroDivisionError:
    #     print("ERROR: Indeterminado")



