from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.crud.feed import CrudFeed
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado

router = APIRouter()

@router.get("/"
# ,response_model=List[UserFeed]
)
async def feed(session: Session = Depends(get_db),
                    #    , current_user: Usuario = Depends(obter_usuario_logado
				page: int = 0
				):
	return CrudFeed(session).feed(2, page)