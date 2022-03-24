from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List

# 

class AutorSimples(BaseModel):
    nome: str

class Autor(AutorSimples):
    id: int

    class Config:
        orm_mode = True