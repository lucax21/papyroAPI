from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

router = APIRouter()

@router.get("/usuarios_test")
async def dados_usuario(db: Session = Depends(get_db)):
    dado = RepositorioUsuario(db).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

