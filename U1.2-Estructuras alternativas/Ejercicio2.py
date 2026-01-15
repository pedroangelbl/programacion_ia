# 2.Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las 
# dimensiones de los lados de un triángulo. El programa debe determinar que 
# tipo de triangulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

side_a = float(input('Dame el lado del triangulo A: '))
side_b = float(input('Dame el lado del triangulo B: '))
side_c = float(input('Dame el lado del triangulo C: '))

if ((side_a**2 + side_b**2) == (side_c**2)):
    print('Se cumple el teorema de pitagoras, por lo tanto es un triangulo rectangulo')
if (side_a == side_b == side_c):
    print('Sus tres lados son iguales por lo tanto es un triangulo equilátero')
elif (side_a == side_b or side_a == side_c or side_b == side_c):
    print('Dos de sus lados son inguales por lo tanto es un triangulo isosceles')
else:
    print('Es un triangulo escaleno')