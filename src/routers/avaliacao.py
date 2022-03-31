from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from src.crud.avaliacao import CrudAvaliacao
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado

router = APIRouter()

@router.get("/{id}")
def carregar_avaliacao(id: int, session: Session = Depends(get_db)):
    return CrudAvaliacao(session).carregar_avaliacao(id)