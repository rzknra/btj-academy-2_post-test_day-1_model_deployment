# Impor library yang dibutuhkan 
import mlflow
import os
from dotenv import load_dotenv

# Load environment variables dari .dev.env
load_dotenv(".dev.env")

# Ambil URL dari env
tracking_uri = os.getenv("MLFLOW_TRACKING_URI")

# Set tracking uri ke MLflow
mlflow.set_tracking_uri(tracking_uri)

MODEL_NAME = "IrisLogRegPipeline"
MODEL_VERSION = "latest"

# URI model dari registry, ambil versi terakhir (Latest staging/production)
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"

# Load model pipeline dari MLflow   
model = mlflow.sklearn.load_model(model_uri)

# Coba prediksi ulang dengan model yang sudah di-load
X_test = [[5.1, 3.5, 1.4, 0.2]]
y_pred = model.predict(X_test)

print("Hasil prediksi:", y_pred)
