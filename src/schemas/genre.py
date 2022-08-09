from __future__ import annotations

from pydantic import BaseModel


class BaseGenre(BaseModel):
    name: str
    description: str


class Genre(BaseGenre):
    id: int

    class Config:
        orm_mode = True


class GenreUserNew(BaseModel):
    idGenero: int
