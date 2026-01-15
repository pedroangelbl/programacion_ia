# 4.Escribir un programa que que calcule el desglose mínimo en billetes 
# y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 
# 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.

amount = int(input('Escriba la cantidad de dinero: '))

values = [500,200,100,50,20,10,5,2,1]

remaining_amount = amount

for value in values:
    value_amount = remaining_amount // value

    if(value_amount > 0):
        if(value >= 5):
            type_ = 'billetes' if value_amount > 1 else 'billete'
        else:
            type_ = 'monedas' if value_amount > 1 else 'moneda'
        
        print(f"{value_amount} {type_} de {value}")
    
        remaining_amount = remaining_amount % value