from __future__ import annotations
from lib2to3.pgen2.token import OP

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date


class UsuarioSimples(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    photo: Optional[str] = None
    description: Optional[str] = None

class UsuarioCriar(UsuarioSimples):
    email: EmailStr
    password: Optional[str] = None
    confirm_password: Optional[str] = None
    birthday: date
    
    class Config:
        orm_mode = True

class UsuarioDb(UsuarioSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Usuario(UsuarioDb):
    descripition: Optional[str] = None
    email: Optional[EmailStr] = None
    birthday: date

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

from src.schemas.livro import Livro

class UsuarioPerfil(UsuarioSimples):
    # descricao: Optional[str] = None
    livros_lendo: List[Livro] = []
    livros_lerei: List[Livro] = []
    livros_lidos: List[Livro] = []
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed  =  True

UsuarioPerfil.update_forward_refs()

