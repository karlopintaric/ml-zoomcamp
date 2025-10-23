from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

app = FastAPI(title="ML model deployment")

with open("pipeline_v1.bin", "rb") as f_in:
    dv, model = pickle.load(f_in)


class Features(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float


class PredictionResponse(BaseModel):
    predicted_probability: float


@app.post("/predict", response_model=PredictionResponse)
def predict_endpoint(features: Features):
    X = dv.transform([features.dict()])
    y_pred = model.predict_proba(X)[:, 1]
    return {"predicted_probability": y_pred[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
