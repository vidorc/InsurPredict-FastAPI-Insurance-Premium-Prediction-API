from fastapi import FastAPI, HTTPException
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()

# human readable
@app.get("/")
def home():
    return {"message": "Insurance Premium Prediction API"}

# machine readable
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "version": MODEL_VERSION,
        "model_loaded": model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
def predict_premium(data: UserInput):
    try:
        # Convert input into dict for model
        user_input = {
            "bmi": data.bmi,
            "age_group": data.age_group,
            "lifestyle_risk": data.lifestyle_risk,
            "city_tier": data.city_tier,
            "income_lpa": data.income_lpa,
            "occupation": data.occupation,
        }

        prediction = predict_output(user_input)

        # ✅ Return schema-compliant response
        return PredictionResponse(response=prediction)

    except Exception as e:
        # ✅ Return proper HTTPException for errors
        raise HTTPException(status_code=500, detail=str(e))
