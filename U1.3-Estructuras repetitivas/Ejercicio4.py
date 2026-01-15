# 4.Escribe un programa que pida el limite inferior y superior de un intervalo. Si
# el límite inferior es mayor que el superior lo tiene que volver a pedir.

# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando
# termine el programa dará las siguientes informaciones:

# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.

while(True):
    lower_limit = int(input('Introduzca el límite inferior: '))
    upper_limit = int(input('Introduzca el límite superior: '))

    if upper_limit > lower_limit:
        break

    print('Vuelve a introducir, el límite inferior no puede ser mayor que el límite superior')

sum_nums = 0
out_range = 0
equal_to_limit = False

while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break

    # Comprobar si está dentro del intervalo abierto
    if lower_limit < num < upper_limit:
        sum_nums += num
    elif num == lower_limit or num == upper_limit:
        equal_to_limit = True
    else:
        out_range += 1

print(f'La suma de los números dentro del intervalo es: {sum_nums}')
print(f'Cantidad de números fuera del intervalo: {out_range}')
print('Hay algún número en el límite' if equal_to_limit else 'No hay números en el límite')