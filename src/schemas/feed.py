from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from src.schemas.user import UserSuperBasic
from src.schemas.book import BookFeed


class Feed(BaseModel):
    rates: Optional[int] = 0
    type: str
    id: int
    you_liked: Optional[bool] = False
    text: Optional[str] = None
    date: Optional[str] = None
    rate: Optional[int] = 0
    likes: Optional[int] = 0
    user: UserSuperBasic
    book: BookFeed
