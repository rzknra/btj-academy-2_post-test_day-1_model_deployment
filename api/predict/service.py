# Import library yang dibutuhkan
import pickle
from api.predict.schema import PredictionParams

# Path model dan scaler
IRIS_MODEL_PATH = "api/predict/models/logistic_regression_model.pkl"
IRIS_SCALER_PATH = "api/predict/models/minmax_scaler.pkl"

# Kelas untuk melakukan prediksi
class Predict:
    def __init__(self, params: PredictionParams):
        self.params = params

    def predict(self):
        pred_data = [[
            self.params.sepal_length,
            self.params.sepal_width,
            self.params.petal_length,
            self.params.petal_width
        ]]

        try:
            # Load model
            with open(IRIS_MODEL_PATH, "rb") as model_file:
                model = pickle.load(model_file)
            # Load scaler
            with open(IRIS_SCALER_PATH, "rb") as scaler_file:
                scaler = pickle.load(scaler_file)
        except FileNotFoundError as e:
            return {"error": f"File model atau scaler tidak ditemukan: {e}"}
        except pickle.UnpicklingError as e:
            return {"error": f"File model atau scaler korup: {e}"}
        except Exception as e:
            return {"error": f"Gagal memuat model atau scaler: {e}"}

        try:
            # Lakukan scaling dan prediksi
            scaled_data = scaler.transform(pred_data)
            prediction = model.predict(scaled_data)
            return {
                "message": "Prediksi berhasil!",
                "result": prediction.tolist()
            }
        except ValueError as e:
            return {"error": f"Prediksi gagal (input error): {e}"}
        except Exception as e:
            return {"error": f"Prediksi gagal (error lain): {e}"}
