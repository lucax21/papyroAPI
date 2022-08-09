from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.crud.genre import CrudGenre
from src.db.database import get_db
from src.db.models.models import User
from src.routers.login_utils import obter_usuario_logado
from src.schemas.genre import Genre, GenreUserNew
from src.schemas.user import UserGenre

router = APIRouter()


@router.get("/", response_model=List[Genre])
async def listar_generos(session: Session = Depends(get_db),
                         current_user: User = Depends(obter_usuario_logado)):
    dado = CrudGenre(session).list_genres()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado


@router.post("/", status_code=status.HTTP_201_CREATED)
def generos_usuario_gravar(lista: List[GenreUserNew], session: Session = Depends(get_db),
                           current_user: User = Depends(obter_usuario_logado)):
    if len(lista) < 3:
        raise HTTPException(status_code=404, detail='Deve haver um mínimo de 3 gêneros literários selecionados.')

    return CrudGenre(session).save_user_genres(lista, current_user.id)


@router.get("/usuarioGeneros", response_model=UserGenre)
async def listar_generos_usuario(session: Session = Depends(get_db),
                                 current_user: User = Depends(obter_usuario_logado)):
    return CrudGenre(session).list_user_genres(current_user.id)
