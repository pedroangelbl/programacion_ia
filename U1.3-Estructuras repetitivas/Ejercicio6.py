# 6.Crea un programa que muestre en pantalla los N primeros número primos. 
# El valor de N se pide por teclado al usuario/a.

def is_prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    
    return is_prime

n_value = int(input('Cuántos números primos quieres mostrar? '))
counter = 0
number = 2
print(f'Los {n_value} primeros números primos son:')

while counter < n_value:
    if is_prime_number(number):
        print(number, end=" ")
        counter += 1
    number += 1
    
