from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def read_root():
    return {"message": "ML Pipeline Active"}

@app.post("/predict")
def predict(data: InputData):
    # Mock inference
    result = data.feature1 * 0.5 + data.feature2 * 0.2
    return {"prediction": result, "status": "success"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
