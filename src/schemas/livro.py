from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

from .autor import Autor


class LivroSimples(BaseModel):
    nome: str
    capa: Optional[str] = None
    chave: Optional[str] = None
    nota: int
    autores: List[Autor] = []

    class Config:
        orm_mode = True


class LivroId(BaseModel):
    id: Optional[int] = None
    identifier: Optional[str] = None
    cover: Optional[str] = None
    book_title: str
    rate: Optional[int]
    raters: Optional[int]
    description: str
    author: List[str]
    reviews: Optional[List]
    genre: Optional[List[str]] = None
    book_status_user: Optional[str] = None

    class Config:
        orm_mode = True


class LivroCriar(LivroId):
    pass


class LivroAvaliar(BaseModel):
    id_livro: int
    nota: int
    texto: str
