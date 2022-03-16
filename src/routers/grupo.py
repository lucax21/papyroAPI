from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from src.crud.grupo import CrudGrupo

from src.db.database import get_db
from src.schemas.grupo import Grupo

router = APIRouter()

@router.post("/",status_code=status.HTTP_201_CREATED)
def criar_grupo():
    pass

@router.get("/buscarGrupos/{termo}",response_model=List[Grupo])
def buscar_grupos(termo: str,session: Session = Depends(get_db)):
    if not termo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")
     
    dado = CrudGrupo(session).buscar_por_grupo(termo)
    if not dado:
        raise HTTPException(status_code=404, detail='Grupo não encontrado')
    return dado

@router.get("/get/{id}",response_model=Grupo)
def buscar_por_id(id: int,session: Session = Depends(get_db)):
    if not id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudGrupo(session).buscar_por_id(id)
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado