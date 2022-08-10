from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class BaseGenre(BaseModel):
    name: str
    description: str


class Genre(BaseGenre):
    id: int

    class Config:
        orm_mode = True

class GenreUser(Genre):
    select_genre: Optional[bool] = None

class GenreUserNew(BaseModel):
    id: int
