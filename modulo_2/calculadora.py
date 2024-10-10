def menu():
    print('Menú calculadora')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Mostrar historial')
    print('6. Salir')

def calculations(operation, num1, num2):
    if operation == 1:
        result = num1 + num2
        operation_str = (f'{num1} + {num2} = {result}') 
    elif operation == 2:
        result = num1 - num2
        operation_str = (f'{num1} - {num2} = {result}') 
    elif operation == 3:
        result = num1 * num2
        operation_str = (f'{num1} * {num2} = {result}')
    elif operation == 4:
        if num2 != 0: 
            result = num1 / num2
            operation_str = (f'{num1} / {num2} = {result}') 
        else: 
            operation_str = 'No se puede divir por cero'
    return operation_str

def historial(history):
    if history:
        print('Historial:')
        for operation in history:
            print (operation)
    else: 
        print('No hay historial')

def calculator():
    history = []
    while True:
        menu()
        option = input('Seleccione una opción: ')
        if option == '1' or option == '2' or option == '3' or option == '4': 
            try:
                num1 = float(input('Ingrese un número: '))
                num2 = float(input('Ingrese un número: '))
            except ValueError:
                print('Ingresar un número válido')
                continue
            operation = int(option)
            result = calculations(operation, num1, num2)
            print(f'{result}')
            history.append(result)
        elif option == '5':
            historial(history)
        elif option == '6':
            print('Fin del programa')
            break
       
        else: 
            print('Opción inválida, intente de nuevo')
calculator()