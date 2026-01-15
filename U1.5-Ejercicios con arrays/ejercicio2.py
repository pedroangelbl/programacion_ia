"""
2. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""

import numpy as np

number = np.random.randint(0, 101, size=20)
square = number ** 2
cube   = number ** 3

print(f"{'NUMBER':>6} {'SQUARE':>10} {'CUBE':>12}")
for n, s, c in zip(number, square, cube):
    print(f"{n:>6} {s:>10} {c:>12}")
