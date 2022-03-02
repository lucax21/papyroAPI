from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List

class LivroSimples(BaseModel):
    nome: str
    capa: str
    nota: int

class Livro(LivroSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True