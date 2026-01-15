# 2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

from math import sqrt

cateto1 = float(input('¿Cuánto mide el cateto a? '))
cateto2 = float(input('¿Cuánto mide el cateto b?' ))

#Formula para calcular la hipotenusa(raiz de la suma de los catetos al cuadrado)
hipotenusa = sqrt(cateto1**2 + cateto2**2)

print('Por lo tanto la hipotenusa mide', hipotenusa)