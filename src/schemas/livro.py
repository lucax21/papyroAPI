from __future__ import annotations

from pydantic import BaseModel
from typing import Optional,List
from datetime import date

from .autor import Autor

class LivroSimples(BaseModel):
    nome: str
    capa: Optional[str] = None
    nota: int
    autores: List[Autor] = []

    class Config:
        orm_mode = True

class Livro(LivroSimples):
    id: Optional[int] = None
    ano: date
    #isbn10: str
    #isbn13: str
    sinopse: str
    # autor
    # generos: List[]

    class Config:
        orm_mode = True

class LivroCriar(Livro):
    pass