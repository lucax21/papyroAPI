from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from src.db.database import get_db
from src.crud.usuario import CrudUsuario


router = APIRouter()

@router.get("/usuariostest")
async def dados_usuario(db: Session = Depends(get_db)):
    dado = CrudUsuario(db).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.get("/meusGeneros")
async def generos_usuario(db: Session = Depends(get_db)):
    dado = CrudUsuario(db).listar_generos()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.get("/gravarGeneros")
async def generos_usuario_gravar(generos_sele: Optional[List[int]] = Query(None),db: Session = Depends(get_db)):
    if not generos_sele:
        return generos_sele
        # raise HTTPException(status_code=404, detail='Deve haver um mínimo de 3 gêneros literários selecionados.')
    return generos_sele