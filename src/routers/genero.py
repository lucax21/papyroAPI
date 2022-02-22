from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from typing import Optional, List
from src.db.database import get_db
from src.crud.genero import CrudGenero
from src.models.models import Usuario
from src.routers.login_utils import obter_usuario_logado
from src.schemas.genero import Genero

router = APIRouter()

@router.get("/", response_model=List[Genero])
async def listar_generos(session: Session = Depends(get_db)):
    dado = CrudGenero(session).listar_generos()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.post("/")
async def generos_usuario_gravar(lista: List[Genero],session: Session = Depends(get_db)):
    #, current_user: Usuario = Depends(obter_usuario_logado)
    id_user = 1
    
    if len(lista) < 3:
        raise HTTPException(status_code=404, detail='Deve haver um mínimo de 3 gêneros literários selecionados.')
    
    dado = CrudGenero(session).salvar_generos_usuario(lista, id_user)
    return dado

@router.get("/{id}/")
async def listar_generos_usuario():
    return "Listar generos usuario"