from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.crud.livro import CrudLivro
from src.db.database import get_db
from src.schemas.livro import LivroId, LivroAvaliar, LivroCriar
from typing import Optional

from src.routers.login_utils import obter_usuario_logado
from src.schemas.usuario import Usuario

router = APIRouter()


@router.get("/", response_model=List[LivroId])
def listar_livros(session: Session = Depends(get_db)):
    dado = CrudLivro(session).listar_livros()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado


@router.get("/buscarLivros/{termo}", response_model=List[LivroId])
def buscar_livro_nome(termo: str, session: Session = Depends(get_db)):
    if not termo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudLivro(session).buscar_por_nome(termo)
    if not dado:
        raise HTTPException(status_code=404, detail='Livro não encontrado')
    return dado

#
@router.get("/{id}", response_model=LivroId)
async def buscar_por_id(id: int, page: int = 0, session: Session = Depends(get_db)):

    if not id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    try:
        current_user = obter_usuario_logado()
    except:
        current_user = None

    dado = CrudLivro(session).buscar_por_id(id, page, current_user)

    return dado


@router.post("/", status_code=status.HTTP_201_CREATED)
def gravar_livro(livro: LivroCriar, session: Session = Depends(get_db)):
    return "Falta implementar"


@router.get("/{id}/pessoas"
            # ,response_model=Livro
            )
def pessoas_livro(id: int, session: Session = Depends(get_db)
                  , current_user: Usuario = Depends(obter_usuario_logado)
                  ):
    return CrudLivro(session).pessoas_livro(id)


@router.post("/avaliar", status_code=status.HTTP_201_CREATED)
def avaliar_livro(ava: LivroAvaliar, session: Session = Depends(get_db)
                  , current_user: Usuario = Depends(obter_usuario_logado)
                  ):
    return CrudLivro(session).avaliar_livro(current_user.id, ava)
