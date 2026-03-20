"""
1.- Queremos hacer una aplicación que sea capaz de convertir una cantidad de dinero 
en una moneda a otra moneda, para ello haremos uso de la API descrita aquí.

Al usuario/a le pediremos:
    La moneda desde la que queremos la conversión.
    La moneda a la que queremos convertir.
    La cantidad de dinero que tenemos.

A tener en cuenta:
    Si la consulta da un error hay que indicarlo.
    Al usuario se le mostrarán las diferentes unidades de moneda antes de pedir los datos, 
    estas se pueden obtener mediante consulta en esta misma API.
"""

import os
import requests
from dotenv import load_dotenv

# Cargamos las variables de entorno de nuestro .env
load_dotenv()
api_key = os.getenv("api_key")
base_url = os.getenv("base_url")

# Método para hacer la petición que te de la conversión
def get_exchange_rate(from_c, to_c, a):
    url = f"{base_url}/{api_key}/pair/{from_c}/{to_c}/{a}"
    try:
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            converted_amount = data['conversion_result']
            return converted_amount

        print("Error en la respuesta de la API")
    except requests.exceptions.RequestException as e:
        print(f"Hubo un error con la petición: {e}")

# 1. Validar que las variables existan antes de seguir
if not api_key or not base_url:
    print("Error: No se encontraron las variables de entorno. Revisa tu archivo .env")
else:
    from_currency = input("Ingresa la moneda de origen: ").upper()
    to_currency = input("Ingresa la moneda a la que quieres convertir: ").upper()
    amount = float(input("Ingresa la cantidad a convertir: "))

    result = get_exchange_rate(from_currency, to_currency, amount)
    if result is not None:
        print(f"La cantidad convertida es: {result}")
