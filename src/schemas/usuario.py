
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date
from src.schemas.genero import Genero

from fastapi import Form

def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

# Propriedades compartilhadas
class UsuarioSimples(BaseModel):
    nome: str
    apelido: str
    foto: Optional[str] = None

# Propriedades a receber via API na criação
@form_body
class UsuarioCriar(UsuarioSimples):
    email: EmailStr
    senha: str
    data_nascimento: date
    
    class Config():
        orm_mode = True

class UsuarioDb(UsuarioSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Usuario(UsuarioDb):
    email: Optional[EmailStr] = None
    data_nascimento: date

class UsuarioGeneros(UsuarioSimples):
    generosLiterarios: List[Genero]