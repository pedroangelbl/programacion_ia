# 7.Crea un programa que nos permita calcular la cuota de una hipoteca y 
# su tabla de amortización después de que se pida al usuario/a:

# Importe del préstamo.
# La tasa de interés anual.
# Y el plazo de pago en años.

amount = float(input('Ingrese el importe del préstamo: '))
annual_rate = float(input('Ingrese la tasa de interés anual (en %): ')) / 100
years = int(input('Ingrese el plazo de pago en años: '))

monthly_rate = annual_rate / 12
months = years * 12

