from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel

from src.schemas.user import UserSuperBasic

class UsersCompanyStatus(BaseModel):
    id: int
    status: str
    readers: Optional[List[UserSuperBasic]] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UsersCompany(BaseModel):
    readers_reading: Optional[UsersCompanyStatus] = None
    readers_read: Optional[UsersCompanyStatus] = None
    readers_to_read: Optional[UsersCompanyStatus] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True