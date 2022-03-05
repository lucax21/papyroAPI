from __future__ import annotations

from pydantic import BaseModel
from typing import Optional
from datetime import date

class LivroSimples(BaseModel):
    nome: str
    capa: str
    nota: int

class Livro(LivroSimples):
    id: Optional[int] = None
    ano: date
    #isbn10: str
    #isbn13: str
    #sinopse: str
    # autor
    # generos: List[]

    class Config:
        orm_mode = True

class LivroCriar(Livro):
    pass