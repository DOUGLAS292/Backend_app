from pydantic import BaseModel, Field
from typing import Optional

class Location(BaseModel):
    lon: float = Field(..., description="Longitud (ej: -76.5300)")
    lat: float = Field(..., description="Latitud (ej: 3.4516)")

class OfferBase(BaseModel):
    client_id: str
    title: str
    description: str
    area_m2: float
    budget_cop: float
    location: Optional[Location] = None

class OfferCreate(OfferBase):
    pass

class Offer(OfferBase):
    id: str
