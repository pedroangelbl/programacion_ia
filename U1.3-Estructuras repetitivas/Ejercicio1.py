# 1.Escribir un programa que imprima todos los números pares entre dos números que se 
# le pidan al usuario.

number1 = int(input('Escribe el primer número: '))
number2 = int(input('Escribe el segundo número: '))

for i in range(number1, number2):
    if i % 2 == 0:
        print(i)
