from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from src.schemas.usuario import UserSuperBasic
from src.schemas.book import BookFeed

class UserFeed(BaseModel):
    count_comments: Optional[int] = 0
    text: Optional[str] = None
    # date: Optional[str] = None
    # rate: Optional[int] = None
    likes: Optional[int] = 0
    user: UserSuperBasic
    book: BookFeed