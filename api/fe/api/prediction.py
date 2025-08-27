# Impor library yang dibutuhkan
import requests
import json
import os
from typing import Dict
from dotenv import load_dotenv

# Load variabel environment
load_dotenv(dotenv_path=".dev.env")

# Ambil variabel environment
URL = os.getenv("APP_HOST")
PORT = os.getenv("APP_PORT")

# Endpoint untuk prediksi
def get_pred(data: Dict):
    req = requests.post(url=f"http://{URL}:{PORT}/predict", json=data)
    result = req.json()

    message = result.get("message", "")
    result = result.get("result", [])
    return message, result
