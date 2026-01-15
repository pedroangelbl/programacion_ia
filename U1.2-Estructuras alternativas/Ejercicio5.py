# 5.Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el 
# día correspondiente. Si introducimos otro número nos da un error.

day = int(input('Pida un dia de la semana segun su número correspondiente (del 1 al 7): '))

week_days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

if ( 1<= day <=7):
    print(week_days[day-1])
else:
    print('Ese número no esta dentro del rango')