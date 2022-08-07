from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.crud.feed import CrudFeed
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.feed import Feed
from typing import List
from src.schemas.usuario import Usuario

router = APIRouter()

@router.get("/"
,response_model=List[Feed]
)
async def feed(session: Session = Depends(get_db),
                current_user: Usuario = Depends(obter_usuario_logado),
				page: int = 0
				):
	return CrudFeed(session).feed(current_user.id, page)