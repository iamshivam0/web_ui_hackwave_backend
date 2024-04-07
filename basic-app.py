from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import gzip

app = FastAPI()

# Load the original machine learning model for weather prediction from a gzipped file
try:
    with gzip.open('random_forest_model.pkl.gz', 'rb') as f:
        weather_model = joblib.load(f)
except FileNotFoundError:
    raise FileNotFoundError("Model file 'random_forest_model.pkl.gz' not found. Please ensure it exists.")

# Define a Pydantic model for the request body for weather prediction
class WeatherRequest(BaseModel):
    Air_temperature: float
    Pressure: float
    Wind_speed : float

# Load the new machine learning model for power prediction from a gzipped file
try:
    with gzip.open('model_sta2.pkl.gz', 'rb') as f:
        power_model = joblib.load(f)
except FileNotFoundError:
    raise FileNotFoundError("Model file 'model_sta.pkl.gz' not found. Please ensure it exists.")

# Define a Pydantic model for the request body for power prediction
class PowerPredictionRequest(BaseModel):
    month: int
    day: int
    time: int
    p1: float
    p2: float
    p3: float
    c1: float
    c2: float
    c3: float
    Total_Power: float


# CORS Configuration
origins = ["*"]  # You can specify allowed origins here, or use "*" to allow all origins

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

# Define route for making predictions with the original model
@app.post("/predict/")
async def predict_weather(data: WeatherRequest):
    # Convert input data to numpy array
    input_data = np.array([[data.Air_temperature, data.Pressure, data.Wind_speed]])

    # Make prediction using the original model
    prediction = weather_model.predict(input_data)

    # Return prediction
    return {"power": prediction[0]}

# Define route for making predictions with the new model
@app.post("/predict/power/")
async def predict_power(data: PowerPredictionRequest):
    # Calculate power distribution for nodes based on the given percentages
    total_power = data.Total_Power
    node1_power = total_power * 0.2
    node2_power = total_power * 0.45
    node3_power = total_power * 0.35

    # Convert input data to numpy array
    input_data = np.array([[data.month, data.day, data.time, node1_power, node2_power, node3_power, data.p1, data.p2, data.p3, data.c1, data.c2, data.c3]])

    # Make prediction using the new model
    prediction = power_model.predict(input_data)

    # Return prediction
    return {"power_prediction": prediction[0]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
