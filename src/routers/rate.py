from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud.rate import CrudAvaliacao
from src.db.database import get_db

router = APIRouter()


@router.get("/{id}")
def carregar_avaliacao(id: int, session: Session = Depends(get_db)):
    return CrudAvaliacao(session).carregar_avaliacao(id)
