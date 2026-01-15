"""
5. Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se 
deben introducir en una lista de 4 rows por 5 columnas. El programa mostrará las sumas 
parciales de rows y columnas igual que si de una hoja de cálculo se tratara. La suma total 
debe aparecer en la esquina inferior derecha.
"""

import random

matriz = []

# Rellenar la matriz 4x5 con números aleatorios
for i in range(4):
    fila = []
    for j in range(5):
        numero = random.randint(100, 999)
        fila.append(numero)
    matriz.append(fila)

# Mostrar matriz + suma de filas
for fila in matriz:
    suma_fila = 0
    for num in fila:
        print(num, end=" ")
        suma_fila += num
    print("|", suma_fila)

print("-------------------------------")

# Suma de columnas
for c in range(5):
    suma_columna = 0
    for f in range(4):
        suma_columna += matriz[f][c]
    print(suma_columna, end=" ")

# Suma total
suma_total = 0
for fila in matriz:
    for num in fila:
        suma_total += num

print("|", suma_total)
