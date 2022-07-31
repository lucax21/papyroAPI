from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.crud.book import CrudBook
from src.db.database import get_db
from src.schemas.book import BookByID

from src.routers.login_utils import obter_usuario_logado
from src.schemas.usuario import Usuario

router = APIRouter()


@router.get("/{id}", response_model=BookByID)
async def get_book_by_id(id: int,
                         page: int = 0,
                         current_user: Usuario = Depends(obter_usuario_logado),
                         session: Session = Depends(get_db)):

    data = CrudBook(session).get_by_id(id, page, current_user.id)

    return data
