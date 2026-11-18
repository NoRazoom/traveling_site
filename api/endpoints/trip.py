import random

from fastapi import APIRouter

from schemas.trip import TripRequest
from services.geoapify import get_random_place

router = APIRouter()

"""@router.post('/random')
async def get_random_place(data: TripRequest):
    # Пока заглушка: потом подставишь реальный геокодер и места
    fake_places = [
        {"name": "Кофейня «Север»", "category": data.category, "distance_km": 3.2},
        {"name": "Парк «Лесной»", "category": data.category, "distance_km": 7.8},
        {"name": "Музей современного искусства", "category": data.category, "distance_km": 12.4},
    ]
    return random.choice(fake_places)"""

@router.post('/random')
async def get_random_trip(data: TripRequest):
    return await get_random_place(
            location=data.location,
            radius_km=data.radius_km,
            category=data.category,
        )