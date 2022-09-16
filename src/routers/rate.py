from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.routers.login_utils import obter_usuario_logado
from src.db.models.models import User
from src.crud.rate import CrudRate
from src.db.database import get_db
from src.schemas.rate import NewRate

router = APIRouter()


@router.post("/")
async def new_rate(data: NewRate, session: Session = Depends(get_db), current_user: User = Depends(obter_usuario_logado)):
    return CrudRate(session).new_rate(current_user.id, data)
