# 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un programa 
# que determine la hora de llegada a la ciudad B.

departure_time = input('Hora de salida en formato HH:MM:SS ')
split_departure_time = departure_time.split(':') #Separamos el input por ':'

hh = int(split_departure_time[0]) #Horas de salida
mm = int(split_departure_time[1]) #Minutos de salida
ss = int(split_departure_time[2]) #Segundos de salida

#Obtenemos el tiempo de viaje hasta llegar a B en segundos
t = int(input('Tiempo de viaje en segundos: '))

#Tiempo de salida en segundos
departure_time_seconds = hh * 3600 + mm * 60 + ss

#Tiempo de llegada en segundos
arrive_time_seconds = departure_time_seconds + t

#Convertir ahora al formato HH:MM:SS
arrive_hh = arrive_time_seconds // 3600
arrive_mm = (arrive_time_seconds % 3600) // 60
arrive_ss = (arrive_time_seconds % 3600) % 60

arrive_time = str(arrive_hh) + ':' + str(arrive_mm) + ':' + str(arrive_ss)

print('La hora de llegada es: ', arrive_time)