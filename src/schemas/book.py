from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel, HttpUrl


class BookBase(BaseModel):
    id: Optional[int] = None
    cover: Optional[str] = None
    book_title: Optional[str] = None
    author: Optional[List[str]] = None
    count: Optional[int] = None

    class Config:
        orm_mode = True


class BookSearch(BookBase):
    id: Optional[int] = None
    rate: Optional[int] = 0
        
    class Config:
        fields = {'count': {'exclude': True}}

class BookExtended(BaseModel):
    id: Optional[int]
    book_title: str
    cover: str
    status: Optional[int] = None
    genre: List[str]
    description: str
    author: List[str]


class BookUser(BaseModel):
    nickname: str
    photo: Optional[str] = 'https://uploads.sarvgyan.com/2014/03/image-unavailable.jpg'
    id: int


class BookReviewBase(BaseModel):
    id: Optional[int]
    date: str
    likes: Optional[int] = 0
    comments: Optional[int] = 0
    rate: Optional[int] = None
    you_like: Optional[bool] = False
    text: str


class BookReview(BookReviewBase):
    user: BookUser


class BookByID(BookExtended):
    identifier: Optional[str] = None
    rate: Optional[int]
    raters: Optional[int] = 0
    reviews: Optional[List[BookReview]] = [None]
    company: Optional[int] = 0

    class Config:
        orm_mode = True


class BookFeed(BaseModel):
    id: Optional[int] = None
    cover: Optional[HttpUrl] = None
    book_title: Optional[str] = None


class BookByType(BaseModel):
    id: Optional[int] = None
    identifier: Optional[str] = None
    cover: Optional[str] = None
    book_title: str
    rate: Optional[int]
    author: List[str]

    class Config:
        orm_mode = True


class BookUserStatus(BaseModel):
    id_user: int
    id_book: int
    id_status: int


class BookSuggestion(BaseModel):
    data: List[BookByType]
