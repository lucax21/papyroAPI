from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List

# 

class GeneroSimples(BaseModel):
    genero: str

class Genero(GeneroSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True 

# class Aa(Genero):
#     usuarios: List[Usuario]

# from src.schemas.usuario import Usuario
# Usuario.update_forward_refs()