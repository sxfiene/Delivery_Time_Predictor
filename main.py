# import csv
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# def load_data(file_path: str):
#     data = []
#     with open(file_path, mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             row["Order_ID"] = int(row["Order_ID"])
#             row["Distance_km"] = float(row["Distance_km"])
#             row["Preparation_Time_min"] = int(row["Preparation_Time_min"])
#             row["Delivery_Time_min"] = int(row["Delivery_Time_min"])
#             data.append(row)
#     return data

# DATA_FILE = "./Delivery_Time_Predictor/Food_Delivery_Times.csv"
# data = load_data(DATA_FILE)

# class Delivery(BaseModel):
#     Order_ID: int
#     Distance_km: float
#     Weather: str
#     Traffic_Level: str
#     Time_of_Day: str
#     Vehicle_Type: str
#     Preparation_Time_min: int
#     Courier_Experience_yrs: float
#     Delivery_Time_min: int

# @app.get("/deliveries")
# def get_deliveries():
#     return {"data": data}

# @app.get("/deliveries/{order_id}")
# def get_delivery_by_id(order_id: int):
#     for delivery in data:
#         if delivery["Order_ID"] == order_id:
#             return {"delivery": delivery}
#     raise HTTPException(status_code=404, detail="Order not found")

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Charger le modèle sauvegardé
model = joblib.load('gbr_pipeline.pkl')


# Définir le format des données d'entrée
class InputData(BaseModel):
    Distance_km: float
    Weather: str
    Traffic_Level: str
    Time_of_Day: str
    Vehicle_Type: str
    Courier_Experience_yrs: float

# Créer l'application FastAPI
app = FastAPI()

# Prétraitement des données (mimique celui utilisé avant entraînement)
def preprocess_input(data: InputData):
    # Convertir les données en DataFrame
    input_dict = data.dict()
    input_df = pd.DataFrame([input_dict])

    # Appliquer les transformations (à adapter selon votre entraînement)
    input_df = input_df.replace({
        "Weather": {"Windy": 0, "Rainy": 1, "Sunny": 2},
        "Traffic_Level": {"Low": 0, "Medium": 1, "High": 2},
        "Time_of_Day": {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3},
        "Vehicle_Type": {"Scooter": 0, "Bike": 1, "Van": 2}
    })

    # Vérifiez que les colonnes sont dans le bon ordre
    return input_df.values

@app.get("/")
def read_root():
    """
    Point d'entrée principal pour vérifier le fonctionnement de l'API.
    """
    return {"message": "Bienvenue sur l'API d'estimation de durée de livraison"}

@app.post("/predict/")
def predict(data: InputData):
    """
    Route pour effectuer des prédictions à partir des données fournies.
    :param data: Données d'entrée au format JSON avec les caractéristiques requises.
    :return: Estimation de la durée de livraison (en minutes).
    """
    try:
        # Prétraiter les données d'entrée
        processed_data = preprocess_input(data)
        # Effectuer une prédiction
        prediction = model.predict(processed_data)
        return {"estimated_delivery_time_min": round(prediction[0], 2)}
    except Exception as e:
        return {"error": str(e)}