from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List

class GrupoSimples(BaseModel):
    nome: str
    foto: Optional[str]
    descricao: str

class Grupo(GrupoSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True