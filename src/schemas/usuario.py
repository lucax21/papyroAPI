from __future__ import annotations
from lib2to3.pgen2.token import OP

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

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
    nome: Optional[str] = None
    apelido: Optional[str] = None
    foto: Optional[str] = None
    descricao: Optional[str] = None

# Propriedades a receber via API na criação
@form_body
class UsuarioCriar(UsuarioSimples):
    email: EmailStr
    senha: Optional[str] = None
    senha_confirmacao: Optional[str] = None
    data_nascimento: date
    
    class Config:
        orm_mode = True

class UsuarioDb(UsuarioSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Usuario(UsuarioDb):
    descricao: Optional[str] = None
    email: Optional[EmailStr] = None
    data_nascimento: date

class UsuarioAddLivroBiblioteca(BaseModel):
    # id_usuario: int
    id_livro: int
    id_status: int

    class Config:
        orm_mode = True

from src.schemas.genero import Genero

class UsuarioGeneros(UsuarioSimples):
    generos: List[Genero] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed  =  True


class AtualizarFoto(BaseModel):
    link: str


UsuarioGeneros.update_forward_refs()

from src.schemas.livro import LivroId

class UsuarioPerfil(UsuarioSimples):
    # descricao: Optional[str] = None
    livros_lendo: List[LivroId] = []
    livros_lerei: List[LivroId] = []
    livros_lidos: List[LivroId] = []
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed  =  True

UsuarioPerfil.update_forward_refs()

