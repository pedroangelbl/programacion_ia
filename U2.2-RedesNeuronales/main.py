from fastapi import FastAPI
from pydantic import BaseModel
import keras
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir que el formulario web (HTML) se comunique con la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el modelo y el escalador
model = keras.models.load_model("model/modelo_vinos.keras")
scaler = joblib.load("model/scaler.pkl")

class WineData(BaseModel):
    features: list  # Recibiremos una lista de 11 valores

@app.post("/predict")
def predict(data: WineData):
    print(data)
    # Convertir a array y escalar
    input_data = np.array([data.features])
    input_scaled = scaler.transform(input_data)

    # Predecir
    prediction = model.predict(input_scaled)

    print(prediction)
    return {"quality": float(prediction[0][0])}
