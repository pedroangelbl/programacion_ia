"""
2.- El FBI tiene recorte de personal informático y solicitan nuestra ayuda, 
quieren saber cuantos fugitivos tienes registrados en cada una de sus oficinas, 
para ello han habilitado una API a la que puedes acceder desde aquí.

El programa debe mostrar el nombre de cada oficina (ordenado) y la cantidad 
de fugitivos registrados. También debe mostrar la cantidad de fugitivos no 
registrados en ninguna oficina. 

Ten en cuenta que cada consulta muestra un número limitado de registros, vas 
a tener que hacer consultas iterativas enviando como parámetro la página de 
la consulta hasta que ya no queden páginas que consultar.
"""

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
        # Recogemos los items de la respuesta del modelo, si no tiene, es vacio ([])
        items = data.get("items", [])

        # Si no hay items rompemos el flujo
        if not items:
            break

        # Iteramos sobre los distintos fugitivos
        for fugitivo in items:
            field_offices = fugitivo.get("field_offices")

            # Vamos sumando los que no tengas oficinas asignadas
            if not field_offices:
                sin_oficina += 1
            else:
                for oficina in field_offices:
                    oficinas[oficina] = oficinas.get(oficina, 0) + 1

        print(f"Procesada página {pagina_actual}...", end="\r")
        pagina_actual += 1

    print("\n\n--RESULTADOS POR OFICINA--")
    # Mostramos los datos ordenados
    for nombre in sorted(oficinas.keys()):
        print(f"{nombre}: {oficinas[nombre]} fugitivos")

    print(f"\nFugitivos sin oficina asignada: {sin_oficina}")


analizar_fugitivos()
