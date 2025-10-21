# 7.Crea un programa que nos permita calcular la cuota de una hipoteca y 
# su tabla de amortización después de que se pida al usuario/a:

# Importe del préstamo.
# La tasa de interés anual.
# Y el plazo de pago en años.
# Solicitar datos al usuario

loan = float(input("Introduce el importe del préstamo: "))
annual_rate = float(input("Introduce la tasa de interés anual (%): "))
years = int(input("Introduce el plazo de pago en años: "))

# Calcular tasa mensual y número de pagos
monthly_rate = annual_rate / 12 / 100
num_payments = years * 12

# Calcular cuota mensual
payment = loan * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

print(f"\nCuota mensual: {payment:.2f}€")
print("\nTabla de amortización:")
print("Mes | Cuota | Interés | Amortización | Capital pendiente")
print("-" * 60)

# Calcular tabla de amortización
remaining_balance = loan
for month in range(1, num_payments + 1):
    interest = remaining_balance * monthly_rate
    principal = payment - interest
    remaining_balance -= principal
    print(f"{month:3d} | {payment:6.2f}€ | {interest:7.2f}€ | {principal:11.2f}€ | {remaining_balance:15.2f}€")
