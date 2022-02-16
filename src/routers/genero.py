from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.crud.genero import CrudGenero

router = APIRouter()

@router.get("/")
async def listar_generos(db: Session = Depends(get_db)):
    dado = CrudGenero(db).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado