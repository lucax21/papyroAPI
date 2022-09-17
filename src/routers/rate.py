from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.utils.login_utils import obter_usuario_logado
from src.db.models.models import User
from src.crud.rate import CrudRate
from src.db.database import get_db
from src.schemas.rate import NewRate, Rate


router = APIRouter()


@router.post("/")
async def new_rate(data: NewRate, session: Session = Depends(get_db), current_user: User = Depends(obter_usuario_logado)):
    return CrudRate(session).new_rate(current_user.id, data)

@router.get("/{rate_id}", response_model=Rate)
async def get_rate(rate_id: int,
                       page: int = 0,
                       current_user: User = Depends(obter_usuario_logado),
                       session: Session = Depends(get_db)):

    return CrudRate(session).get_rate(rate_id, current_user.id, page)
