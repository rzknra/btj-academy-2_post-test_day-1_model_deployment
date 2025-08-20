# =========================================================
# Import library yang dibutuhkan
# =========================================================
import os  # Untuk mengakses variabel lingkungan
from typing import Union  # Untuk tipe data opsional pada endpoint

import pandas as pd  # Bisa digunakan jika nanti memproses data
from dotenv import load_dotenv  # Untuk load file .env
from fastapi import FastAPI  # Framework FastAPI

# =========================================================
# Load environment variables dari file .dev.env
# =========================================================
load_dotenv(dotenv_path=".dev.env")
api_key = os.getenv("GITHUB_API")  # Contoh penggunaan API key

# =========================================================
# Inisialisasi aplikasi FastAPI
# =========================================================
app = FastAPI(
    title="TEST PROJECT 1",
    description="Contoh project FastAPI sederhana",
    version="1.0.0"
)

# =========================================================
# Endpoint root
# =========================================================
@app.get("/")
def read_root():
    """
    Endpoint untuk menguji apakah API berjalan
    """
    return {"message": "Hello World"}

# =========================================================
# Endpoint untuk membaca item
# =========================================================
@app.get("/items/{item_id}")
def read_item(
    item_id: int,  # Parameter path: ID item
    q: Union[str, None] = None  # Parameter query opsional
):
    """
    Endpoint untuk mengembalikan item tertentu
    """
    return {"item_id": item_id, "q": q}

# =========================================================
# Endpoint untuk prediksi (dummy)
# =========================================================
@app.get("/predict/")
def predict(
    data_id: int,  # ID data
    val: int       # Nilai input
):
    """
    Endpoint dummy untuk prediksi model
    """
    # Contoh hasil prediksi statis
    result = "Model has been predicted with result TRUE"

    return {
        "data_id": data_id,
        "val": val,
        "result": result
    }
