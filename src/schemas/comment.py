from __future__ import annotations

from typing import Optional, List
from fastapi import HTTPException, status
from pydantic import BaseModel, validator

from src.schemas.book import BookExtended, BookUser, BookReviewBase


class Comment(BaseModel):
    id: int
    likes: Optional[int] = 0
    date: str
    text: str
    you_liked: Optional[bool] = False
    user: BookUser


class Comments(BaseModel):
    book: BookExtended
    review: BookReviewBase
    reviewer: BookUser
    comments: Optional[List[Comment]] = [None]


class NewComment(BaseModel):
    rate_id: int
    text: str

    @validator('text')
    def vl_password(cls, value):
        if not value or len(value) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Comentário muito curto.")
        return value


class CommentReturn(BaseModel):
    comment_id: int
