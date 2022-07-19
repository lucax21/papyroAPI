from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from src.crud.comentario import CrudComentario
from src.db.database import get_db
from src.db.models.models import Comment
from src.routers.login_utils import obter_usuario_logado
from src.schemas.comentario import ComentarioSalvar

router = APIRouter()

@router.post("/")
def salvar_comentario(dado: ComentarioSalvar, session: Session = Depends(get_db)):
    if not dado.texto:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insira uma Mensagem para enviar.")
    return CrudComentario(session).salvar_comentario(24,dado)