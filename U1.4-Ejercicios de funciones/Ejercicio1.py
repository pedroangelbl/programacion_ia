"""Ejercicio 1

Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco
opciones: sumar, restar, multiplicar, dividir y terminar. Cada opción llama a una función
a la que se le pasan las dos variables y muestra el resultado de la operación. Si se introduce
una opción incorrecta se muestra un mensaje de error. El menú se volverá a mostrar, a menos que 
no se de a la opción terminar.

Modifica el programa anterior para que la introducción de las variables sea una opción del menú
(la primera). Las variables se inicializan a cero.

Modifica el programa anterior para que si no se introducen las dos variables desde la opción
correspondiente no se puedan ejecutar el resto de las opciones.

Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas,
pide una opción (por su número) y devuelve la opción escogida. Modifica el último programa 
para que use esta función.

"""


def get_values():
    while True:
        try:
            a = int(input("Dame el valor de a: "))
            b = int(input("Dame el valor de b: "))
            return a, b
        except ValueError:
            print("Por favor, introduzca un número válido")


def show_menu(options):
    a = 0
    b = 0
    values_entered = False

    while True:
        print("\n --- Menu de opciones ---")
        for key, value in options.items():
            name, function = value
            print(f"{key}. {name}")

        option = input("Seleccione una opción: ")

        if option in options:
            if option == "0":
                print("Hasta luego!!!")
                break
            if option == "1":
                a, b = get_values()
                values_entered = True
            elif values_entered:
                name, function = options[option]
                function(a, b)
            else:
                print("Primero debes introducir los valores")
        else:
            print("Opción inválida")


def add(a, b):
    result = a + b
    print("El resultado de sumar a y b es: ", result)


def subtract(a, b):
    result = a - b
    print("El resultado de restar a y b es: ", result)


def multiply(a, b):
    result = a * b
    print("El resultado de multiplicar a y b es: ", result)


def divide(a, b):
    result = a / b
    print("El resultado de dividir a y b es: ", result)


def main():
    options = {
        "0": ("Terminar", None),
        "1": ("Pedir valores", get_values),
        "2": ("Sumar", add),
        "3": ("Restar", subtract),
        "4": ("Multiplicar", multiply),
        "5": ("Dividir", divide),
    }
    show_menu(options)


if __name__ == "__main__":
    main()
