# Impor library yang dibutuhkan
import pandas as pd
import mlflow
import mlflow.sklearn
import os

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, accuracy_score, f1_score, recall_score
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables dari .dev.env
load_dotenv(".dev.env")

# Ambil URL dari env
tracking_uri = os.getenv("MODEL_TRACKING_URI")

# Set tracking uri dan experiment ke MLflow
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment("Iris_Classification_Experiment")

# Nama model di registry & artifact
MODEL_NAME = "IrisLogRegPipeline"
ARTIFACT_PATH = "iris_logreg_pipeline"

# Load Dataset
iris = load_iris(as_frame=True)
X = iris.data.astype(float)  
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Pipeline dengan parameter terbaik
pipeline = Pipeline([
    ("scaler", MinMaxScaler()),
    ("model", LogisticRegression(
        solver="lbfgs",     
        penalty=None,               
        max_iter=200,       
        random_state=42
    ))
])

# Jalankan run MLflow
timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
run_name = f"LogReg_BestParams_{timestamp}"

with mlflow.start_run(run_name=run_name) as run:
    pipeline.fit(X_train, y_train)

    # Evaluasi di test set
    y_pred = pipeline.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred, average="macro")
    f1 = f1_score(y_test, y_pred, average="macro")

    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {acc:.4f} | Recall: {rec:.4f} | F1 Score: {f1:.4f}")

    # Log params (best params)
    mlflow.log_params({
        "solver": "lbfgs",
        "penalty": None,
        "max_iter": 200
    })

    # Log metrics
    mlflow.log_metrics({
        "accuracy": acc,
        "recall": rec,
        "f1_score": f1
    })

    # Log model ke registry
    mlflow.sklearn.log_model(
        sk_model=pipeline,
        name=ARTIFACT_PATH,
        registered_model_name=MODEL_NAME,
        input_example=X_test
    )

print("Training selesai. Model dicatat ke MLflow registry.")
