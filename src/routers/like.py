from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.crud.like import CrudLike
from src.db.database import get_db
from src.utils.login_utils import obter_usuario_logado
from src.schemas.user import User

router = APIRouter()


@router.patch("/{like_type}/{id}/{mode}")
async def like(id: int, like_type: str, mode: bool,
               current_user: User = Depends(obter_usuario_logado),
               session: Session = Depends(get_db)):
    if like_type != 'r' and like_type != 'c':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Argumento de tipo de post inválido.")

    return CrudLike(session).like_by_id(id, like_type, current_user.id, mode)
