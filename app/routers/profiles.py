from fastapi import APIRouter, HTTPException
from app.core.supabase_client import supabase
from app.schemas.profile import Profile, ProfileCreate

router = APIRouter(prefix="/profiles", tags=["Profiles"])

@router.post("/", response_model=Profile)
def create_profile(profile: ProfileCreate):
    data = profile.dict()

    try:
        result = supabase.table("Perfiles").insert(data).execute()
        if not result.data:
            raise HTTPException(status_code=400, detail="Error insertando el perfil")
        return result.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear perfil: {str(e)}")


@router.get("/{user_id}", response_model=Profile)
def get_profile(user_id: str):
    result = supabase.table("Perfiles").select("*").eq("id", user_id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return result.data[0]
