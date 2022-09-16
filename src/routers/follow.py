from typing import List, Optional

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.crud.follow import CrudFollow
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.follow import Follow
from src.schemas.user import User

router = APIRouter()


@router.get("/"
    , response_model=List[Follow]
            )
async def get_follow(
        follow_type: str,
        user_id: Optional[int] = None,
        page: int = 0,
        current_user: User = Depends(obter_usuario_logado),
        session: Session = Depends(get_db)):
    if not user_id:
        user_id = current_user.id
    return CrudFollow(session).get_follow(user_id, follow_type, page)


@router.post("/{id_follow}/{mode}")
async def add_or_remove_follow(
        id_follow: int,
        mode: bool,
        current_user: User = Depends(obter_usuario_logado),
        session: Session = Depends(get_db)):
    return CrudFollow(session).add_remove_follow(current_user.id, id_follow, mode)
