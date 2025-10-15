from fastapi import APIRouter, HTTPException
from app.core.supabase_client import supabase
from app.schemas.offer import Offer, OfferCreate

router = APIRouter()

@router.post("/", response_model=Offer)
def create_offer(offer: OfferCreate):
    insert_payload = offer.dict()

    # ✅ Convertir location a formato PostGIS (WKT con SRID)
    if offer.location:
        lon = offer.location.lon
        lat = offer.location.lat
        insert_payload["location"] = f"SRID=4326;POINT({lon} {lat})"

    result = supabase.table("offers").insert(insert_payload).execute()

    if result.data:
        return result.data[0]

    raise HTTPException(status_code=400, detail=result.error_message)
