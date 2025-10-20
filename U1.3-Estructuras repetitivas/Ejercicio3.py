# 3.Crea una aplicación que permita adivinar un número. La aplicación genera 
# un número aleatorio del 1 al 100. A continuación va pidiendo números y va 
# respondiendo si el número a adivinar es mayor o menor que el introducido, además 
# de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa 
# termina cuando se acierta el número (además te dice en cuantos intentos lo has 
# acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

random_number = random.randint(1,100)
print(random_number)

for i in range(10):
    try_ = int(input(f'Intento número {i+1}. Introduzca un número del 1 al 100: '))

    if(try_ > random_number):
        print('El número ha adivinar es menor')
    elif(try_ < random_number):
        print('El número ha adivinar es mayor')
    elif(try_ == random_number):
        print(f'Enhorabuena has acertado, te ha costado {i+1} intentos')
        break
    
    if(i+1 == 10):
        print(f'Lo siento, el número a acertar era el {random_number}')