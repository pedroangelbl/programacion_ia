# 7.Realiza un programa que pida cinco números enteros y diga cuál es el mayor 
# No se puede usar la función max()..

higher = None 

for i in range(5):
    number = int(input(f"Introduzca el número {i+1}: "))

    if (higher is None or number > higher):
        higher = number
    
print(f"El número mayor es {higher}")