from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    full_name: str
    role: str
    profession: Optional[str] = None
    city: Optional[str] = None  # Aquí guardas la ciudad
    bio: Optional[str] = None
    experience_years: Optional[int] = 0
    phone: Optional[str] = None
    image_url: Optional[str] = None
    rating_avg: Optional[float] = 0.0
    rating_count: Optional[int] = 0

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: Optional[str] = None
