from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud.feed import CrudFeed
from src.db.database import get_db
from src.utils.login_utils import obter_usuario_logado
from src.schemas.feed import Feed
from src.schemas.user import User

router = APIRouter()


@router.get("/", response_model=List[Feed])
async def get_feed(session: Session = Depends(get_db),
               current_user: User = Depends(obter_usuario_logado),
               page: int = 0):
    return CrudFeed(session).get_feed(current_user.id, page)
