# 5.Crea un programa que pida un número por teclado al usuario y diga
# si es primo. En caso de que no se introduzca un número o que esta sea
# menor que 2 se debe mostrar un mensaje de error.

number = int(input("Introduzca un número para comprobar si es un número primo: "))

if number <= 1:
    print("Error, el número debe ser mayor o igual que 2")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"El número {number} es primo")
    else:
        print(f"El número {number} no es primo")
