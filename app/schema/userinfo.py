from pydantic import BaseModel, UUID4, EmailStr
from typing import Optional


class UserInfo(BaseModel):
    id: UUID4
    email: EmailStr
    username: str
    profile_picture: Optional[str] = None
