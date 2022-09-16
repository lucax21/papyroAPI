from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.crud.user_book import CrudUserBook
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.book import BookUserStatus, BookByType
from src.schemas.user import User
from src.schemas.user_book import UsersCompany, UsersCompanyStatus
from src.utils.enum.reading_type import ReadingTypes
from typing import List, Optional

router = APIRouter()

@router.patch("/{id_book}/{id_status}"
, response_model=BookUserStatus
)
async def book_user_status(
        id_book: int,
        id_status: Optional[int],
        user_id: Optional[int] = None,
        current_user: User = Depends(obter_usuario_logado),
        session: Session = Depends(get_db)):
    if id_status != ReadingTypes.READING and id_status != ReadingTypes.READ and id_status != ReadingTypes.TO_READ and id_status != 0:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Status do livro inválido.")
    if not user_id:
        user_id = current_user.id
    return CrudUserBook(session).book_user_status(user_id, id_status, id_book)


@router.get("/{id}/companionship", response_model=UsersCompany)
async def get_companionship(id: int, session: Session = Depends(get_db)):
    return CrudUserBook(session).get_companionship(id)


@router.get("/books/{reading_type}", response_model=List[BookByType])
def get_user_books(reading_type: str,
                   user_id: Optional[int] = None,
                   page: int = 0,
                   current_user: User = Depends(obter_usuario_logado),
                   session: Session = Depends(get_db)):
    if not user_id:
        user_id = current_user.id

    if reading_type == 'reading':
        return CrudUserBook(session).user_books(user_id, ReadingTypes.READING, page)
    if reading_type == 'read':
        return CrudUserBook(session).user_books(user_id, ReadingTypes.READ, page)
    if reading_type == 'to_read':
        return CrudUserBook(session).user_books(user_id, ReadingTypes.TO_READ, page)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passe o parâmetro de leitura.")


@router.get("/{id_book}/{id_status}", response_model=UsersCompanyStatus)
async def get_companionship_status(
        id_book: int,
        id_status: int,
        page: int = 0,
        session: Session = Depends(get_db)):
    if id_status != ReadingTypes.READING and id_status != ReadingTypes.READ and id_status != ReadingTypes.TO_READ:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Status do livro inválido.")

    return CrudUserBook(session).get_companionship_status(id_book, id_status, page)

