from __future__ import annotations
import re
from typing import Optional, List

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, validator, HttpUrl

from src.schemas.book import BookByID
from src.schemas.genre import Genre


class BaseUser(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    photo: Optional[str] = 'https://i.pinimg.com/736x/67/4f/c5/674fc554838de6abdbf274bdc0ca446c.jpg'
    description: Optional[str] = None


class UserID(BaseModel):
    id: int


class UserDB(BaseUser):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserDB):
    description: Optional[str] = None
    booksQt: Optional[int] = None
    followers: Optional[int] = None


class NewUser(BaseModel):
    name: str
    nickname: str
    email: EmailStr
    password: str
    confirmation_password: str

    
    @validator('password')
    def vl_password(cls, value):
        password = re.match('^(?=\\S+$).{8,32}$', value)
        if not password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A senha deve conter no mínimo 8 dígitos e no máximo 32 dígitos.")
        return value
    
    @validator('confirmation_password')
    def vl_confirmation_password(cls,v , values, **kwargs):
        if 'password' in values and v != values['password']:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A senhas são diferentes.")
        
    class Config:
        orm_mode = True
        fields = {'description': {'exclude': True}}

class UserPhoto(BaseModel):
    photo: HttpUrl

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str
    nickname: str
    description: str

    @validator('nickname')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'deve ser alfanumérico'
        return v


class Usuario(UserDB):
    booksQt: Optional[int] = None
    followers: Optional[int] = None
    you_follow: Optional[bool] = False


class UserSuperBasic(BaseModel):
    id: int
    nickname: str
    photo: Optional[HttpUrl] = 'https://i.pinimg.com/736x/67/4f/c5/674fc554838de6abdbf274bdc0ca446c.jpg'

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserSearch(UserSuperBasic):
    common_genre: Optional[int] = 0
    common_book: Optional[int] = 0


class UserSuggestion(UserSuperBasic):
    interactions: Optional[int] = 0


class Suggestion(BaseModel):
    data: List[UserSuggestion]


class UserAddBookToLibrary(BaseModel):
    id_livro: int
    id_status: int

    class Config:
        orm_mode = True


class UserGenre(BaseUser):
    genres: List[Genre] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


UserGenre.update_forward_refs()


class UserProfile(BaseUser):
    reading_books: List[BookByID] = []
    to_read_book: List[BookByID] = []
    read_books: List[BookByID] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


UserProfile.update_forward_refs()


