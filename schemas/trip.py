from pydantic import BaseModel, Field


class TripRequest(BaseModel):
    location: str
    radius_km: int = Field(ge=1, le=500)
    category: str