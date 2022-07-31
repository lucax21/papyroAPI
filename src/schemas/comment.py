from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel

from src.schemas.book import BookExtended, BookReview, BookUser, BookReviewBase


class Comment(BaseModel):
    id: int
    likes: Optional[int] = 0
    date: str
    text: str
    you_liked: Optional[bool] = False


class CommentList(BaseModel):
    user: BookUser
    comment: Comment


class Comments(BaseModel):
    book: BookExtended
    review: BookReviewBase
    reviewer: BookUser
    comments: Optional[List[CommentList]] = [None]
