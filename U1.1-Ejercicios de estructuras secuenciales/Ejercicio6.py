# 6. Escribir un programa para calcular la nota final de un examen, considerando que:
# Cada respuesta correcta suma 5 puntos.
# Cada respuesta incorrecta suma -1 puntos.
# Cada respuesta en blanco suma 0 puntos. 
# Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

RIGHT_SCORE = 5

total_answers = int(input('Número de preguntas totales: '))
correct_answers = int(input('Respuestas correctas: '))
incorrect_answers = int(input('Respuestas incorrectas: '))

# Calcular puntuación total
total_score = correct_answers * RIGHT_SCORE - incorrect_answers * 1

# Calcular nota sobre 10
max_score = total_answers * RIGHT_SCORE
normalized_score = (total_score / max_score) * 10

# Evitar notas negativas
if normalized_score < 0:
    normalized_score = 0

print('La nota final normalizada es: ', normalized_score)
