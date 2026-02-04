import requests


def analizar_fugitivos():
    url = "https://api.fbi.gov/wanted/v1/list"
    oficinas = {}
    sin_oficina = 0
    pagina_actual = 1

    print("Consultando datos del FBI (esto puede tardar un poco)...")

    while True:
        # Hacemos la petición a la página actual
        params = {"page": pagina_actual}
        response = requests.get(url, params=params)

        if response.status_code != 200:
            print(f"Error al acceder a la API: {response.status_code}")
            break

        data = response.json()
        items = data.get("items", [])

        if not items:
            break

        for fugitivo in items:
            field_offices = fugitivo.get("field_offices")

            if not field_offices:
                sin_oficina += 1
            else:
                for oficina in field_offices:
                    oficinas[oficina] = oficinas.get(oficina, 0) + 1

        print(f"Procesada página {pagina_actual}...", end="\r")
        pagina_actual += 1

    print("\n\n--RESULTADOS POR OFICINA--")
    for nombre in sorted(oficinas.keys()):
        print(f"{nombre}: {oficinas[nombre]} fugitivos")

    print(f"\nFugitivos sin oficina asignada: {sin_oficina}")


analizar_fugitivos()
