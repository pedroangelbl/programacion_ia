from ejercicio1 import Duration
from ejercicio2 import Fraction

t1 = Duration(1, 21, 30)
t2 = Duration(1, 20, 90)
t3 = t1 + t2
t4 = t2 - t1

if t1 > t2:
    print("es mayor")
elif t1 <= t2:
    print("es menor o igual")

print(t3)
print(t4)

# ------------------------------------------

f1 = Fraction(5, 3)
f2 = Fraction(3, 3)
f3 = 5 * f1
f4 = 2 + f2 - 1
f5 = 1 / f2

if 1 != f2:
    print("no es igual")
elif f1 < 3:
    print("f1 es menor")

print(f1)
print(f2)
print(f3)
print(f4)
print(f5)
