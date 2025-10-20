# 2.Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
# números a introducir). El programa debe informar de cuantos números introducidos 
# son mayores que 0, menores que 0 e iguales a 0.

number_amount = int(input('Cantidad de números a introducir: '))

print(f'{number_amount} números a introducir')

greater_numbers = 0
lower_numbers = 0
equal_numbers = 0

for i in range(number_amount):
    number = int(input(f'Introduce el numero {i}: '))
    numbers = [number]

    if (number > 0):
        greater_numbers += 1
    elif (number < 0):
        lower_numbers += 1
    else:
        equal_numbers += 1
    
    greater_numbers_words = 'número es mayor' if greater_numbers == 1 else 'números son mayores'
    lower_number_words = 'número es menor' if lower_numbers == 1 else 'números son menores'
    equal_number_words = 'número es igual' if equal_numbers == 1 else 'números son iguales'

print(f'{greater_numbers} {greater_numbers_words}, {lower_numbers} {lower_number_words} y {equal_numbers} {equal_number_words}')