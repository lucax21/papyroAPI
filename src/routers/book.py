from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.crud.book import CrudBook
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.book import BookSearch, BookByID, BookUserStatus, BookByType, BookSuggestion
from src.schemas.user import User
from src.utils.enum.reading_type import ReadingTypes
from typing import List, Optional

router = APIRouter()


@router.get("/{id}", response_model=BookByID)
async def get_book(id: int,
                         page: int = 0,
                         current_user: User = Depends(obter_usuario_logado),
                         session: Session = Depends(get_db)):
    data = CrudBook(session).get_book(id, page, current_user.id)

    return data


@router.get("/search/"
    , response_model=List[BookSearch]
            )
async def search_book(search: str,
                      page: int = 0,
                      current_user: User = Depends(obter_usuario_logado),
                      session: Session = Depends(get_db)):
    return CrudBook(session).search_book(search, page)


@router.get("/extras/suggestion/get", response_model=BookSuggestion)
async def get_suggestion(page: Optional[int] = 0,
                         current_user: User = Depends(obter_usuario_logado),
                         session: Session = Depends(get_db)):
    return CrudBook(session).get_suggestions(current_user.id, page)