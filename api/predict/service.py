import pickle
from api.predict.schema import PredictionParams

# Path model dan scaler
IRIS_MODEL_PATH = "api/predict/models/logistic_regression_model.pkl"
IRIS_SCALER_PATH = "api/predict/models/minmax_scaler.pkl"

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

        # Load model dan scaler
        with open(IRIS_MODEL_PATH, "rb") as model_file:
            model = pickle.load(model_file)
        with open(IRIS_SCALER_PATH, "rb") as scaler_file:
            scaler = pickle.load(scaler_file)

        # Lakukan scaling dan prediksi
        scaled_data = scaler.transform(pred_data)
        prediction = model.predict(scaled_data)

        return {
            "result": prediction.tolist(),
            "data": f"Prediction process for data "
                    f"{self.params.sepal_length}, {self.params.sepal_width}, "
                    f"{self.params.petal_length}, {self.params.petal_width}"
        }
