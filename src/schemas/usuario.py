from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    apelido: str
    email: str
    senha: str
    data_nascimento: datetime
    foto: Optional[str] = None

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    apelido: str
    email: str
    data_nascimento: datetime
    foto: Optional[str] = None
    
    class Config:
        orm_mode = True
