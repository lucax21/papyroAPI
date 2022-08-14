from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.user import User
from src.schemas.friend import Friend
from src.crud.friend import CrudFriend

router = APIRouter()

@router.get("/", response_model=List[Friend])
async def get_friends(
        page: int = 0,
        #, current_user: User = Depends(obter_usuario_logado)
        session: Session = Depends(get_db)):
    return CrudFriend(session).get_friends(2, page)
