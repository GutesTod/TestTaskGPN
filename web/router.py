from fastapi import APIRouter, Depends
from web.models import *
from database.models import *
from sqlalchemy.orm import Session
from typing import List
from database.backend import get_db

test_router = APIRouter()

@test_router.get("/analysis/all", response_model=List[ValueAnalysis])
async def get_all_analysis(session: Session = Depends(get_db)):
    # Получение всех измерений
    measurements = session.query(Value).all()

    # Вычисление агрегированных показателей
    min_value = min(m.x for m in measurements)
    max_value = max(m.x for m in measurements)
    count = len(measurements)
    sum_value = sum(m.x for m in measurements)
    median_value = sorted(m.x for m in measurements)[count // 2]

    return {
        "min": min_value,
        "max": max_value,
        "count": count,
        "sum": sum_value,
        "median": median_value,
    }

# Маршрут для получения анализа по конкретному пользователю
@test_router.get("/analysis/user/{user_id}", response_model=List[ValueAnalysis])
async def get_user_analysis(
    user_id: int, session: Session = Depends(get_db)
):
    # Получение всех устройств пользователя
    devices = session.query(Device).filter(Device.user_id == user_id).all()

    # Анализ по каждому устройству
    device_analyses = []
    for device in devices:
        measurements = session.query(Value).filter(
            Value.device_id == device.id
        ).all()

        min_value = min(m.x for m in measurements)
        max_value = max(m.x for m in measurements)
        count = len(measurements)
        sum_value = sum(m.x for m in measurements)
        median_value = sorted(m.x for m in measurements)[count // 2]

        device_analyses.append(
            {
                "device_id": device.id,
                "min": min_value,
                "max": max_value,
                "count": count,
                "sum": sum_value,
                "median": median_value,
            }
        )

    return device_analyses

@test_router.post("/devices/", response_model=DeviceCreate)
async def add_device(device: DeviceCreate, session: Session = Depends(get_db)):
    device_in = Device(**device.model_dump())
    session.add(device_in)
    session.commit()
    return device

@test_router.post("/users/", response_model=UserCreate)
async def add_user(user: UserCreate, session: Session = Depends(get_db)):
    user_in = User(**user.model_dump())
    session.add(user_in)
    session.commit()
    return user

@test_router.post("/values/", response_model=ValueCreate)
async def add_measurement(value: ValueCreate, session: Session = Depends(get_db)):
    measurement_in = Value(**value.model_dump())
    session.add(measurement_in)
    session.commit()
    return measurement_in