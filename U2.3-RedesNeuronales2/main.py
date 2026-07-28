from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Permitir que el formulario HTML se comunique con la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el modelo guardado de MNIST (ajusta la ruta si es necesario)
# Nota: Si lo guardaste como .h5 o .keras, pon la extensión correspondiente
try:
    model = tf.keras.models.load_model("fashion_mnist.keras")
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}. Asegúrate de que el archivo existe.")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # 1. Leer los bytes del archivo subido
    contents = await file.read()
    
    # 2. Abrir la imagen usando Pillow
    image = Image.open(io.BytesIO(contents))
    
    # 3. Transformación requerida: Convertir a escala de grises ('L' = 8 bits, 0-255)
    image = image.convert('L')
    
    # 4. Transformación requerida: Redimensionar a 20x20 píxeles
    image = image.resize((20, 20))
    
    # 5. Convertir a un array de NumPy
    img_array = np.array(image)
    
    # --- NOTA IMPORTANTE ---
    # El dataset MNIST original usa fondo negro (0) y trazo blanco (255).
    # Si los usuarios suben fotos de papel blanco con trazo negro, el modelo fallará.
    # Opcional: Invertir colores si el píxel de la esquina es muy claro (fondo blanco)
    if img_array[0, 0] > 128:
        img_array = 255 - img_array
    
    # 6. Normalizar los píxeles (0 a 1) si tu modelo fue entrenado así
    img_array = img_array / 255.0
    
    # 7. Adaptar la forma (Shape) para la entrada de la red neuronal.
    # Dependiendo de tu modelo, puede pedir un vector aplanado de 400 (20x20) 
    # o una matriz con canales (1, 20, 20) o (1, 20, 20, 1).
    # Ajustamos a (1, 20, 20) asumiendo una capa Flatten() al inicio del modelo:
    input_data = np.expand_dims(img_array, axis=0) 
    
    # Si tu red esperaba una entrada aplanada desde el principio (MLP sin Flatten manual), usa:
    # input_data = img_array.reshape(1, 400)

    # 8. Realizar la predicción
    prediction = model.predict(input_data)
    digit_predicted = int(np.argmax(prediction[0]))
    confidence = float(np.max(prediction[0]))

    return {
        "digit": digit_predicted,
        "confidence": confidence
    }
