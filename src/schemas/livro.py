from __future__ import annotations

from pydantic import BaseModel
from typing import Optional,List

class LivroSimples(BaseModel):
    id: Optional[int] = None
    cover: Optional[str] = None
    book_title: Optional[str] = None
    author: Optional[List[str]] = None
    count: Optional[int] = None

    class Config:
        orm_mode = True

class Livro(LivroSimples):
    pass

class LivroCriar(Livro):
    pass

class LivroAvaliar(BaseModel):
    id_livro: int
    nota: int
    texto: str
