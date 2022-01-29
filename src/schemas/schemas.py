from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    apelido: str
    email: str
    senha: str
    data_nascimento: Optional[datetime] = None
    foto: str

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    nome: str
    apelido: str
    email: str
    
    class Config:
        orm_mode = True

class Login(BaseModel):
    senha: str
    email: str

class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str