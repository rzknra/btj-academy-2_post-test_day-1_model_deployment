# File schema.py digunakan untuk validasi input dan output

# Impor library yang diperlukan
from typing import List
from pydantic import BaseModel

# Definisikan skema input untuk permintaan prediksi
class PredictionParams(BaseModel):
    sepal_length: int = 0
    sepal_width: int = 0
    petal_length: int = 0
    petal_width: int = 0

# Definisikan skema output untuk hasil prediksi
class PredictionResult(BaseModel):
    message: str
    result: List[int]
