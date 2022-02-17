from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.crud.genero import CrudGenero
from src.schemas.genero import Genero

router = APIRouter()

@router.get("/", response_model=Genero)
async def listar_generos(db: Session = Depends(get_db)):
    dado = CrudGenero(db).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado