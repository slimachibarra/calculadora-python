# Funciones para testear
def sumar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def calculadora():
    print("Calculadora simple")
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elegí una opción (1/2/3/4): ")

    try:
        num1 = float(input("Ingresá el primer número: "))
        num2 = float(input("Ingresá el segundo número: "))
    except ValueError:
        print("Error: tenés que ingresar números válidos.")
        return

    if opcion == "1":
        resultado = num1 + num2
        print("Resultado:", resultado)

    elif opcion == "2":
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcion == "3":
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcion == "4":
        if num2 == 0:
            print("Error: no se puede dividir por cero.")
        else:
            resultado = num1 / num2
            print("Resultado:", resultado)

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    calculadora()