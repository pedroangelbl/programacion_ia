"""
5. Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se 
deben introducir en una lista de 4 rows por 5 columnas. El programa mostrará las sumas 
parciales de rows y columnas igual que si de una hoja de cálculo se tratara. La suma total 
debe aparecer en la esquina inferior derecha.
"""

import random

matrix = []
for i in range(4):
    row = []
    for j in range(5):
        num = random.randint(100, 999)
        row.append(num)
    matrix.append(row)

sum_rows = []
for row in matrix:
    sum_rows.append(sum(row))
