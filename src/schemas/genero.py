from __future__ import annotations

from pydantic import BaseModel
from typing import Optional, List

# 

class GeneroSimples(BaseModel):
    name: str
    description: str

class Genero(GeneroSimples):
    id: int

    class Config:
        orm_mode = True

class GeneroUsuarioCriar(BaseModel):
    idGenero: int
    

# class GeneroUsuarios(Genero):
#     usuarios: List[Usuario] = []

#     class Config:
#         orm_mode = True 

# from .usuario import Usuario
# Usuario.update_forward_refs()
