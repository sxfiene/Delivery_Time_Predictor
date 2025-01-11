import mlflow
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# Set the MLflow tracking URI
mlflow.set_tracking_uri("http://localhost:8050")

app = FastAPI()

# Initialize the model version counter
model_version = 1

class Delivery(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: int
    Courier_Experience_yrs: float

def load_model(version):
    return mlflow.sklearn.load_model(f"models:/DeliveryTimeModel/{version}")

@app.post("/predict/")
def predict_delivery_time(delivery: Delivery):
    global model_version

    # Load the model from the MLflow Model Registry
    model = load_model(model_version)

    features = pd.DataFrame([{
        "Distance_km": delivery.Distance_km,
        "Weather": delivery.Weather,
        "Traffic_Level": delivery.Traffic_Level,
        "Time_of_Day": delivery.Time_of_Day,
        "Vehicle_Type": delivery.Vehicle_Type,
        "Preparation_Time_min": delivery.Preparation_Time_min,
        "Courier_Experience_yrs": delivery.Courier_Experience_yrs
    }])

    predicted_time = model.predict(features)[0]

    # Increment the model version for the next prediction
    model_version += 1

    return {"predicted_delivery_time": round(predicted_time, 2)}