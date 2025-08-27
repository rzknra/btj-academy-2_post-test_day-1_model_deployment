# Import library yang dibutuhkan
from typing import List
from pydantic import BaseModel, Field

# Model untuk input prediksi
class PredictionParams(BaseModel):
    sepal_length: float = Field(..., ge=0, description="Sepal length dalam cm (>=0)")
    sepal_width:  float = Field(..., ge=0, description="Sepal width dalam cm (>=0)")
    petal_length: float = Field(..., ge=0, description="Petal length dalam cm (>=0)")
    petal_width:  float = Field(..., ge=0, description="Petal width dalam cm (>=0)")

# Model untuk output prediksi
class PredictionResult(BaseModel):
    message: str
    result: List[float] = []
