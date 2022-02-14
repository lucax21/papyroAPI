from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.crud.usuario import CrudUsuario

router = APIRouter()

@router.get("/usuarios_test")
async def dados_usuario(db: Session = Depends(get_db)):
    dado = CrudUsuario(db).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

