
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

from src.schemas.genero import Genero

# Propriedades compartilhadas
class UsuarioSimples(BaseModel):
    nome: str
    apelido: str
    foto: Optional[str] = None

# Propriedades a receber via API na criação
class UsuarioCriar(UsuarioSimples):
    email: EmailStr
    senha: str
    data_nascimento: date

class UsuarioDb(UsuarioSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Usuario(UsuarioDb):
    email: Optional[EmailStr] = None
    data_nascimento: date

class UsuarioGeneros(UsuarioSimples):
    generos: List[Genero]