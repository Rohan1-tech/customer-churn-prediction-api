from fastapi import FastAPI
import numpy as np

from app.schema import ChurnRequest
from app.model_loader import model, scaler, threshold, feature_order

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict(data: ChurnRequest):

    input_data = np.array([[getattr(data, col) for col in feature_order]])

    scaled_data = scaler.transform(input_data)

    prob = model.predict_proba(scaled_data)[0][1]

    prediction = int(prob >= threshold)

    return {
        "churn_probability": float(prob),
        "prediction": prediction
    }