
from calculadoramod.calcu.operaciones import suma, resta, multiplicacion, division
from calculadoramod.calcu.historial import mostrar_historial, agregar_historial


def main():
    while True:
        print('Menú calculadora')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Mostrar historial')
        print('6. Salir')
        option = input("Selecciona una opción: ")

        if option in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
    
            if option == '1':
                result = suma(num1, num2)
                operation_str = (f'{num1} + {num2} = {result}') 
            elif option == '2':
                result = resta(num1, num2)
                operation_str = (f'{num1} - {num2} = {result}')
            elif option == '3':
                result = multiplicacion(num1, num2)
                operation_str = (f'{num1} * {num2} = {result}')
            elif option == '4':
                result = division(num1, num2)
                operation_str = (f'{num1} / {num2} = {result}') 

            print(operation_str)
            agregar_historial(operation_str)    
    
        elif option == '5':
            print("Historial de operaciones:")
            for operacion in mostrar_historial():
                print(operacion)

        elif option == '6':
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
