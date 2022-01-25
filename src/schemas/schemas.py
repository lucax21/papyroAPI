from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    apelido: str
    email: str
    senha: str
    dataNascimento: Optional[datetime] = None
    foto: str

    class Config:
        orm_mode = True
