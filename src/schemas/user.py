from __future__ import annotations
import re, datetime
from datetime import date
from typing import Optional, List

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, validator, HttpUrl

from src.schemas.book import BookByID, BookBase
from src.schemas.genre import Genre


class BaseUser(BaseModel):
    name: Optional[str] = None
    nickname: Optional[str] = None
    photo: Optional[str] = None
    description: Optional[str] = None
    birthday: Optional[str] = None


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


class NewUser(BaseUser):
    email: EmailStr
    password: Optional[str] = None
    confirm_password: Optional[str] = None
    birthday: str
 
    @validator('birthday')
    def vl_birthday(cls, value):
        # verifica se é maior de 18 anos
        value = datetime.datetime.strptime(value, "%d/%m/%Y").date()
        idade = (date.today() - value)
        if (idade.days / 365.25) < 18.0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Você deve ser maior de idade para criar um conta.")
        return value
    
    @validator('password')
    def vl_password(cls, value):
        password = re.match('^(?=\\S+$).{8,32}$', value)
        if not password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A senha deve conter no mínimo 8 dígitos e no máximo 32 dígitos.")
        return value
    
    @validator('confirm_password')
    def vl_confirm_password(cls,v , values, **kwargs):
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
    birthday: str
    
    @validator('birthday')
    def vl_birthday(cls, value):
        #verifica se é maior de 18 anos
        value = datetime.datetime.strptime(value, "%d/%m/%Y").date()
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


class Usuario(UserDB):
    booksQt: Optional[int] = None
    followers: Optional[int] = None
    books_reading: Optional[List[BookBase]] = None
    books_read: Optional[List[BookBase]] = None
    books_to_read: Optional[List[BookBase]] = None


class UserSuperBasic(BaseModel):
    id: int
    nickname: str
    photo: Optional[HttpUrl] = 'https://uploads.sarvgyan.com/2014/03/image-unavailable.jpg'

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserSearch(UserSuperBasic):
	common_genre: Optional[int] = 0
	common_book: Optional[int] = 0


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


class UsersCompanyStatus(BaseModel):
    id: int
    status: str
    readers: Optional[List[UserSuperBasic]] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UsersCompany(BaseModel):
    readers_reading: Optional[UsersCompanyStatus] = None
    readers_read: Optional[UsersCompanyStatus] = None
    readers_to_read: Optional[UsersCompanyStatus] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
