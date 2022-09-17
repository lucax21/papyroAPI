from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.utils.login_utils import obter_usuario_logado
from src.schemas.user import User
from src.schemas.notification import Notification
from src.crud.notification import CrudNotification

router = APIRouter()

@router.get("/"
         , response_model=List[Notification]
        )
async def get_notification(session: Session = Depends(get_db),
        current_user: User = Depends(obter_usuario_logado),
                        page: int = 0):

    return CrudNotification(session).get_notification(current_user.id ,page)

