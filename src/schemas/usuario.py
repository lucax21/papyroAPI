from __future__ import annotations

from datetime import date
from typing import Optional, List

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, validator, HttpUrl

from .livro import LivroSimples


class UsuarioSimples(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    photo: Optional[str] = None
    description: Optional[str] = None
    birthday: Optional[str] = None


class UsuarioCriar(UsuarioSimples):
    email: EmailStr
    password: Optional[str] = None
    confirm_password: Optional[str] = None

    class Config:
        orm_mode = True


class UserPhoto(BaseModel):
    photo: HttpUrl

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str
    nickname: str
    photo: Optional[str] = None
    description: Optional[str] = None
    birthday: date

    @validator('birthday')
    def vl_birthday(cls, value):
        # verifica se é maior de 18 anos
        idade = (date.today() - value)
        if (idade.days / 365.25) < 18.0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Você deve ser maior de idade para criar um conta.")
        return value

    @validator('nickname')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'deve ser alfanumérico'
        return v

    # class Config:
    #     orm_mode = True


class UsuarioDb(UsuarioSimples):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Usuario(UsuarioDb):
    description: Optional[str] = None
    birthday: Optional[str] = None
    booksQt: Optional[int] = None
    followers: Optional[int] = None
    books_reading: Optional[List[LivroSimples]] = None
    books_read: Optional[List[LivroSimples]] = None
    books_to_read: Optional[List[LivroSimples]] = None


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


UsuarioGeneros.update_forward_refs()

from src.schemas.livro import LivroId


class UsuarioPerfil(UsuarioSimples):
    # descricao: Optional[str] = None
    livros_lendo: List[LivroId] = []
    livros_lerei: List[LivroId] = []
    livros_lidos: List[LivroId] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


UsuarioPerfil.update_forward_refs()
