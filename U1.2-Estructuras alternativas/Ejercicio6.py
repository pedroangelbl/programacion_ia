# 6.Realiza un programa que pida tres números enteros y diga cuál es el mayor. 
# No se puede usar la función max().

number1 = int(input('Escriba el primer número'))
number2 = int(input('Escriba el segundo número'))
number3 = int(input('Escriba el tercer número'))

if (number2 < number1 > number3):
    print('El primer número es el mayor')
elif (number1 < number2 > number3):
    print('El segundo número es el mayor')
else:
    print('El tercer número es el mayor')
