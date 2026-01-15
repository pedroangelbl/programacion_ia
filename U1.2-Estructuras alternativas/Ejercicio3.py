# 3.Escribir un programa que lea un año indicar si es bisiesto (un año es 
# bisiesto si es un número divisible por 4, pero no si es divisible por 100, 
# excepto que también sea divisible por 400).

year = int(input('¿Qué año quieres calcular si es bisiesto? '))

if (year % 4 == 0 and year % 100 != 0):
    print('El número es bisiesto')
elif (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print('El número es bisiesto')
else:
    print('El número no es bisiesto')
