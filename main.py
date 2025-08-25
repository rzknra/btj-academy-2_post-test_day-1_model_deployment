# Import library yang dibutuhkaniImport os
from fastapi import FastAPI
from dotenv import load_dotenv
from api.predict.views import predict_router
from api.scheduler.views import scheduler_router

# Muat variabel environment
load_dotenv(dotenv_path=".dev.env")

# Inisialisasi FastAPI
app = FastAPI(title="Iris Prediction API")

# Inisialisasi router
app.include_router(predict_router)
app.include_router(scheduler_router)

# Inisialisasi endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}