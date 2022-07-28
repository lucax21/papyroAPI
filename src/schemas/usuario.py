from __future__ import annotations

from datetime import date
from typing import Optional, List

from pydantic import BaseModel, EmailStr

from .book import BookBase


class UsuarioSimples(BaseModel):
    name: str
    nickname: str
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
    description: Optional[str] = None
    birthday: Optional[str] = None
    booksQt: Optional[int] = None
    followers: Optional[int] = None
    books_reading: Optional[List[BookBase]] = None
    books_read: Optional[List[BookBase]] = None
    books_to_read: Optional[List[BookBase]] = None


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
        arbitrary_types_allowed = True


class AtualizarFoto(BaseModel):
    link: str


UsuarioGeneros.update_forward_refs()

from src.schemas.book import BookByID


class UsuarioPerfil(UsuarioSimples):
    # descricao: Optional[str] = None
    livros_lendo: List[BookByID] = []
    livros_lerei: List[BookByID] = []
    livros_lidos: List[BookByID] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


UsuarioPerfil.update_forward_refs()
