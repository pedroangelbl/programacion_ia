"""
3. Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y
que los almacene en un array de numpy. El programa debe ser capaz de pasar todos
los números pares a las primeras posiciones del array (del 0 en adelante) y todos
los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.
"""

import numpy as np

arr = np.random.randint(0, 101, size=20)

even = arr[arr % 2 == 0]
odd  = arr[arr % 2 != 0]

result = np.concatenate((even, odd))

print("Array original:")
print(arr)

print("\nArray con pares primero y luego impares:")
print(result)
