from __future__ import annotations
from typing import Optional
from xmlrpc.client import boolean
from pydantic import BaseModel
from src.schemas.usuario import UserSuperBasic
from src.schemas.book import BookFeed

class Feed(BaseModel):
    rates: Optional[int] = 0
    type: str
    id: int
    date: str
    rate: int
    you_liked: Optional[bool] = False
    text: Optional[str] = None
    # date: Optional[str] = None
    # rate: Optional[int] = None
    likes: Optional[int] = 0
    user: UserSuperBasic
    book: BookFeed
