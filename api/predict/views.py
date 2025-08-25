# Impor library yang diperlukan
from fastapi import APIRouter
from api.predict.service import Predict   # relative import
from api.predict.schema import PredictionParams, PredictionResult  # relative import

# Inisialisasi router
predict_router = APIRouter()
tag = ["Predict"]

@predict_router.post("/predict", tags=tag)
def predict_route(data: PredictionParams):
    predict = Predict(params=data)
    pred = predict.predict()
    return PredictionResult(
        message=pred.get('data', ""),
        result=pred.get("result")  
    )