"""
6. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""

import numpy as np

# Generar matriz 4x5 con números entre 100 y 999
matriz = np.random.randint(100, 1000, size=(4, 5))

# Sumas de filas y columnas
sumas_filas = matriz.sum(axis=1)
sumas_columnas = matriz.sum(axis=0)

# Suma total
suma_total = matriz.sum()

# Mostrar matriz con sumas de filas
for i in range(4):
    for j in range(5):
        print(matriz[i, j], end=" ")
    print("|", sumas_filas[i])

print("-------------------------------")

# Mostrar sumas de columnas + total
for suma in sumas_columnas:
    print(suma, end=" ")

print("|", suma_total)
