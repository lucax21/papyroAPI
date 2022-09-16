from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.crud.genre import CrudGenre
from src.db.database import get_db
from src.db.models.models import User
from src.routers.login_utils import obter_usuario_logado
from src.schemas.genre import Genre, GenreUserNew, GenreUser

router = APIRouter()


@router.patch("/save/{id}/{mode}")
async def save_user_genre(
        id: int, mode: bool,
        current_user: User = Depends(obter_usuario_logado),
        session: Session = Depends(get_db)):
    return CrudGenre(session).save_user_genres(current_user.id, id, mode)

@router.get("/userGenre", response_model=List[GenreUser])
async def get_list_user_genre(session: Session = Depends(get_db)
                         ,current_user: User = Depends(obter_usuario_logado)
                         ):
    return CrudGenre(session).get_list_user_genres(current_user.id)
