# Impor library yang diperlukan
from fastapi import APIRouter
from api.predict.service import Predict
from api.predict.schema import PredictionParams, PredictionResult

# Inisialisasi router
predict_router = APIRouter()
tag = ["Predict"]

@predict_router.post("/predict", tags=tag, response_model=PredictionResult)
def predict_route(data: PredictionParams):

    try:
        # Jalankan prediksi
        predict = Predict(params=data)
        pred = predict.predict()

        # Validasi hasil prediksi
        if (not isinstance(pred, dict)) or ("result" not in pred) or ("message" not in pred): 
            return PredictionResult(
                message="Format hasil prediksi tidak valid",
                result=[]
            )

        # Jika berhasil
        return PredictionResult(
            message=pred.get("message", ""),
            result=pred.get("result", [])
        )

    except Exception as e:
        # Tangkap error lain dan kembalikan dalam format PredictionResult
        return PredictionResult(
            message=f"Terjadi kesalahan saat prediksi: {str(e)}",
            result=[]
        )

@predict_router.post("/predict_mlflow", tags=tag, response_model=PredictionResult)
def predict_route(data: PredictionParams):

    try:
        # Jalankan prediksi
        predict = Predict(params=data)
        pred = predict.predict_mlflow()

        # Validasi hasil prediksi
        if (not isinstance(pred, dict)) or ("result" not in pred) or ("message" not in pred): 
            return PredictionResult(
                message="Format hasil prediksi tidak valid",
                result=[]
            )

        # Jika berhasil
        return PredictionResult(
            message=pred.get("message", ""),
            result=pred.get("result", [])
        )

    except Exception as e:
        # Tangkap error lain dan kembalikan dalam format PredictionResult
        return PredictionResult(
            message=f"Terjadi kesalahan saat prediksi: {str(e)}",
            result=[]
        )
