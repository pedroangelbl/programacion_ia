# 1.Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o
# la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber
#  con un mensaje adecuado.

first_age = int(input('¿Cuál es la edad de la primera persona?'))
second_age = int(input('¿Cuál es la edad de la segunda persona?'))

if first_age < second_age:
    print('La primera persona es más joven')
elif first_age == second_age:
    print('Ambos tienen la misma edad')
else:
    print('La segunda persona es más joven')
