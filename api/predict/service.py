# Import library yang dibutuhkan
import mlflow
import pickle
import os
from api.predict.schema import PredictionParams
from dotenv import load_dotenv

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
   
    def predict_mlflow(self):
        try:
            # Load environment
            load_dotenv(dotenv_path=".dev.env")
            mlflow_uri = os.getenv("MLFLOW_TRACKING_URI")
            if not mlflow_uri:
                raise ValueError("MLFLOW_TRACKING_URI tidak ditemukan di environment")

            mlflow.set_tracking_uri(mlflow_uri)

            # Load model dari MLflow
            model_uri = "models:/IrisLogRegPipeline/latest"
            model = mlflow.sklearn.load_model(model_uri)

            # Siapkan input dan prediksi
            X_input = [[
                self.params.sepal_length,
                self.params.sepal_width,
                self.params.petal_length,
                self.params.petal_width
            ]]
            y_pred = model.predict(X_input)

            # Ubah hasil prediksi ke list (aman untuk semua tipe iterable)
            result_list = list(y_pred)

            return {
                "message": "Prediksi berhasil!",
                "result": result_list
            }

        except Exception as e:
            return {"message": f"Gagal memprediksi: {e}", "result": None}
