# 3. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

time = int(input('Cantidad de tiempo en minutos: '))

#Cálculo de horas y minutos
hours = time // 60
minutes = time % 60

hour_word = 'horas' if hours != 1 else 'hora'
minute_word = 'minutos' if minutes != 1 else 'minuto'

print('Esto equivale a', hours, hour_word, 'y', minutes, minute_word)