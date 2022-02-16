from pydantic import BaseModel
from typing import Optional

class GeneroSimples(BaseModel):
    genero: str

class Genero(GeneroSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True 

