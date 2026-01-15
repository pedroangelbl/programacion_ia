# 8.Diseña un programa que, dado un número real que debe representar la calificación numérica
# de un examen, proporcione la calificación cualitativa correspondiente al número dado.
# La calificación cualitativa será una de las siguientes: «Suspenso» (nota menor que 5),
# «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual
# que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10),
# «Matrícula de Honor» (nota 10).

score = int(input('Dime tu calificación númerica del examen: '))

if (0 <= score < 5):
    print('Tienes un suspenso')
elif (5 <= score < 7):
    print('Tienes un aprobado')
elif (7 <= score < 9):
    print('Tienes un notable')
elif (9 <= score < 10):
    print('Tienes un sobresaliente')
elif (score == 10):
    print('¡Enhorabuena tienes matricula de honor!')
else:
    print('Introduce una calificación del 0 al 10')