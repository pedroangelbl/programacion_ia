# 4. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

number = input('Dime un número de dos cifras: ')

#Para un número de mas cifras no sería lo mas óptimo
first_number = number[0]
secont_number = number[1]

inverted_number = int(secont_number + first_number)

print('El número invertido es', inverted_number)