"""
3.- Crea una función call_llm(prompt, temperature, max_tokens, system=None, stop=None) 
que haga POST a: https://router.huggingface.co/v1/chat/completions

Haz 3 experimentos con el mismo prompt:
    temp = 0.0
    temp = 0.7
    temp = 1.0
y compara: longitud, estilo, consistencia.

Extrae y muestra solo:
    choices[0].message.content
    usage (tokens) si viene (y comenta qué significa para coste/latencia)

Robustez mínima:
    si status ≠ 200, imprimir status_code + response.text y clasificar si es 401/429/402.

Entrega
    Un mini “Prompt Lab” que imprime una tabla final con columnas:
    temperature | tokens_total | caracteres_respuesta 
"""


import os
from dotenv import load_dotenv
import requests

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")


def call_llm(prompt, temperature, max_tokens, system=None, stop=None):
    url = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    # Cargamos los mensajes del system(como se comporta el modelo) y del usuario(user)
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    # Mandamos el payload con los datos que necesita el modelo
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stop": stop,
    }

    # Respuesta del modelo
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        status = response.status_code
        error_msg = response.text
        # Clasificación de errores comunes
        tipo = "Error Desconocido"
        if status == 401:
            tipo = "No autorizado (Token inválido)"
        elif status == 402:
            tipo = "Pago requerido / Sin créditos"
        elif status == 429:
            tipo = "Límite de peticiones excedido (Rate Limit)"

        print(f"--- ERROR {status}: {tipo} ---")
        print(error_msg)
        return None

    return response.json()


prompt_test = "Cuentame un cuento de un niño que se perdio en el bosque en dos frases, responde solo con eso."
temperaturas = [0.0, 0.7, 1.0]
resultados = []

# Probamos con las diferentes temperaturas y los guardamos en un array
for temp in temperaturas:
    data = call_llm(prompt=prompt_test, temperature=temp, max_tokens=150)

    if data:
        contenido = data["choices"][0]["message"]["content"].strip()

        print(contenido + "\n")

        usage = data.get("usage", {})
        total_tokens = usage.get("total_tokens", "N/A")

        resultados.append(
            {
                "temp": temp,
                "tokens": total_tokens,
                "caracteres": len(contenido),
                "respuesta": contenido,
            }
        )

# TEST Y GRAFICAMOS
print("\n" + "-" * 60)
print(f"{'TEMPERATURE':<12} | {'TOKENS TOTAL':<12} | {'CARACTERES RTDA.'}")
print("-" * 60)

for r in resultados:
    print(f"{r['temp']:<12} | {r['tokens']:<12} | {r['caracteres']}")

print("=" * 60)

# - Un mayor uso de tokens(total_tokens) implica un mayor consumo de cuota/dinero.
# - A su vez, mientras más tokens de salida se tengan que procesar, mayor será el
# tiempo de respuesta, es decir, la latencia
