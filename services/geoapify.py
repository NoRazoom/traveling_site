import os
import random

import httpx
from dotenv import load_dotenv
from fastapi import HTTPException

from core.constants import CATEGORY_MAP, GEOCODING_URL, PLACES_URL

load_dotenv()

GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")


async def geocode_location(location: str) -> tuple[float, float]:
    """Превращает строку с адресом или городом в координаты (lat, lon)."""

    params = {
        "text": location,
        "apiKey": GEOAPIFY_API_KEY,
        "limit": 1,
        "lang": "ru",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(GEOCODING_URL, params=params)
        response.raise_for_status()

        features = response.json().get("features", [])

    if not features:
        raise HTTPException(
            status_code=404,
            detail="Не удалось определить координаты указанного места",
        )

    lon, lat = features[0]["geometry"]["coordinates"]
    return lat, lon


async def get_random_place(
    location: str,
    radius_km: int,
    category: str,
) -> dict:
    """Ищет случайное место выбранной категории в радиусе от точки."""

    geoapify_category = CATEGORY_MAP.get(category)

    if not geoapify_category:
        raise HTTPException(
            status_code=400,
            detail="Неизвестная категория места",
        )

    lat, lon = await geocode_location(location)

    params = {
        "categories": geoapify_category,
        "filter": f"circle:{lon},{lat},{radius_km * 1000}",
        "bias": f"proximity:{lon},{lat}",
        "limit": 20,
        "apiKey": GEOAPIFY_API_KEY,
        "lang": "ru",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(PLACES_URL, params=params)
        response.raise_for_status()

        features = response.json().get("features", [])

    if not features:
        raise HTTPException(
            status_code=404,
            detail="По выбранной категории в радиусе ничего не найдено",
        )

    place = random.choice(features)
    properties = place["properties"]
    lon_place, lat_place = place["geometry"]["coordinates"]

    return {
        "name": properties.get("name") or "Название не указано",
        "category": category,
        "address": properties.get("formatted"),
        "lat": lat_place,
        "lon": lon_place,
        "distance_km": (properties.get("distance") or 0) / 1000,
        "place_id": properties.get("place_id"),
    }