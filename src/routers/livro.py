from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.crud.livro import CrudLivro
from src.db.database import get_db
from src.schemas.livro import Livro

router = APIRouter()

@router.get("/",response_model=List[Livro])
def listar_livros(session: Session = Depends(get_db)):
    dado = CrudLivro(session).listar_livros()
    if not dado:
         raise HTTPException(status_code=404, detail='Não encontrado')
    return dado
