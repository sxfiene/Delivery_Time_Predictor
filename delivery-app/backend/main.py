import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

model = joblib.load("gbr_pipeline.pkl")

class Delivery(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Preparation_Time_min: int
    Courier_Experience_yrs: float

@app.post("/predict/")
def predict_delivery_time(delivery: Delivery):
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

    return {"predicted_delivery_time": round(predicted_time, 2)}