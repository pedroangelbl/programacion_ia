# 7.Realiza un programa que pida cinco números enteros y diga cuál es el mayor 
# No se puede usar la función max().

# Pedir los números
number1 = int(input("Introduzca el número 1: "))
number2 = int(input("Introduzca el número 2: "))
number3 = int(input("Introduzca el número 3: "))
number4 = int(input("Introduzca el número 4: "))
number5 = int(input("Introduzca el número 5: "))

higher = number1

if number2 > higher:
    higher = number2
if number3 > higher:
    higher = number3
if number4 > higher:
    higher = number4
if number5 > higher:
    higher = number5

print(f"El número mayor es: {higher}")
