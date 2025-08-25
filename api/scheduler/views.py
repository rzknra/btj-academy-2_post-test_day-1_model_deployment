# Import library yang diperlukan
from fastapi import APIRouter
from api.scheduler.service import Schedule

# Inisialisasi router
scheduler_router = APIRouter()
tag = ["Schedule"]

@scheduler_router.post("/add_data", tags=tag)
def schedule_route(data: float):
    schedule = Schedule(data)
    return schedule.add_data()
