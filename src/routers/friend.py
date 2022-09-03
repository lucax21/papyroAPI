from typing import List, Optional

from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session

from src.crud.friend import CrudFriend
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.friend import Friend
from src.schemas.user import User

router = APIRouter()


@router.get("/"
    , response_model=List[Friend]
            )
async def get_friends(
        friend_type: str,
        user_id: Optional[int] = None,
        page: int = 0,
        current_user: User = Depends(obter_usuario_logado),
        session: Session = Depends(get_db)):
    if not user_id:
        user_id = current_user.id
    return CrudFriend(session).get_friends(user_id, friend_type, page)


@router.patch("/{oper_type}/{mode}/{id_friend}")
async def accept_or_ignored_friend(
        oper_type: str, mode: bool, id_friend: int,
        session: Session = Depends(get_db),
        current_user: User = Depends(obter_usuario_logado)):
    if oper_type != 'a' and oper_type != 'i':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Argumento de tipo de post inválido.")

    return CrudFriend(session).accept_or_ignored_friend(current_user.id, oper_type, mode, id_friend)


@router.post("/{id_friend}")
async def add_friend(
        id_friend: int,
        current_user: User = Depends(obter_usuario_logado),
        session: Session = Depends(get_db)):
    return CrudFriend(session).add_friend(current_user.id, id_friend)
