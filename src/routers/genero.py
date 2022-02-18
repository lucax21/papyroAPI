from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from typing import Optional, List
from src.db.database import get_db
from src.crud.genero import CrudGenero
from src.schemas.genero import Genero

router = APIRouter()

@router.get("/", response_model=Genero)
async def listar_generos(db: Session = Depends(get_db)):
    dado = CrudGenero(db).listar_generos()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.post("/")
async def generos_usuario_gravar(session: Session = Depends(get_db)):
    
        #raise HTTPException(status_code=404, detail='Deve haver um mínimo de 3 gêneros literários selecionados.')
    
    #dado = CrudGenero(session).salvar_generos(generos_sele)
    return "kkk"

@router.get("/{id}/")
async def listar_generos_usuario():
    return "Listar generos usuario"