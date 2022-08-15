from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.user import User
from src.crud.notification import CrudNotification

router = APIRouter()

@router.get("/")
async def notification(session: Session = Depends(get_db),
        #current_user: User = Depends(obter_usuario_logado),
                        page: int = 0):

    return CrudNotification(session).notification(2, page)
