from pydantic import BaseModel, HttpUrl
from src.schemas.user import UserSuperBasic
from typing import Optional

class Friend(BaseModel):
    id: int
    nickname: str
    photo: Optional[HttpUrl] = None
