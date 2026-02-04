import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")


def call_llm(prompt, temperature, max_tokens, system=None, stop=None):
    url = "https://router.huggingface.co/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = {
        "model": "meta-llama/Llama-3.2-3B-Instruct",
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stop": stop,
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        status = response.status_code
        error_msg = response.text
        # Clasificación de errores comunes
        tipo = "Error Desconocido"
        if status == 401:
            tipo = "No autorizado (Token inválido)"
        elif status == 429:
            tipo = "Límite de peticiones excedido (Rate Limit)"
        elif status == 402:
            tipo = "Pago requerido / Sin créditos"

        print(f"--- ERROR {status}: {tipo} ---")
        print(error_msg)
        return None

    return response.json()


prompt_test = "Cuentame un cuento de un niño que se perdio en el bosque en dos frases, responde solo con eso."
temperaturas = [0.0, 0.7, 1.0]
resultados = []


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

print("\n" + "-" * 60)
print(f"{'TEMPERATURE':<12} | {'TOKENS TOTAL':<12} | {'CARACTERES RTDA.'}")
print("-" * 60)

for r in resultados:
    print(f"{r['temp']:<12} | {r['tokens']:<12} | {r['caracteres']}")

print("=" * 60)

# - Un mayor uso de tokens(total_tokens) implica un mayor consumo de cuota/dinero.
# - A su vez, mientras más tokens de salida se tengan que procesar, mayor será el
# tiempo de respuesta, es decir, la latencia
