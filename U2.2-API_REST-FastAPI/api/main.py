"""
1.- Guardar el modelo en un fichero pickle.

2.- Crear un servicio web usando FastAPI que permita hacer consultas del tipo de flor Iris
pasándole mediante GET las características de la misma (ancho y alto del pétalo y sépalo).
Elegir bien el nombre del endpoint y tener en cuenta que el servicio recibe y devuelve un json.

3.- Mediante Postman o con programas en python, probad el funcionamiento del servicio web.

4.- Crear un formulario HTML que nos permita hacer la consulta anterior.
"""

import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI(title="Flor Iris")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


with open("./models/rf_classifier.pkl", "rb") as f:
    model = pickle.load(f)

target_names = ["setosa", "versicolor", "virginica"]


@app.get("/predict/iris", tags=["Flor Iris"])
def predict_iris(
    sepal_length: float, sepal_width: float, petal_length: float, petal_width: float
):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction = model.predict(features)[0]

    return {
        "input_features": {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        },
        "prediction": int(prediction),
        "species": target_names[int(prediction)],
    }
