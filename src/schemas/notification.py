from __future__ import annotations
from pydantic import BaseModel
from typing import Optional
from src.schemas.user import UserSuperBasic
from src.schemas.book import BookFeed

class NotificationBase(BaseModel):
    id_rate: Optional[int] = None
    text: str
    date: str
    type: str

class Notification(BaseModel):
    book: Optional[BookFeed] = None
    user: UserSuperBasic
    notification: NotificationBase

