from fastapi import FastAPI
from schema import IrisFeatures, PredictionResponce
from model import predicts

app = FastAPI()

@app.post("/predicts", response_model=PredictionResponce)
def classify_iris(features: IrisFeatures):
    result = predicts(features)
    return {"predicted_class": result}


