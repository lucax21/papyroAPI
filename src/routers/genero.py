from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from src.db.database import get_db
from src.crud.genero import CrudGenero
from src.db.models.models import User
from src.routers.login_utils import obter_usuario_logado
from src.schemas.genero import Genero, GeneroUsuarioCriar
from src.schemas.usuario import UsuarioGeneros

router = APIRouter()

@router.get("/"
# , response_model=List[Genero]
)
async def listar_generos(session: Session = Depends(get_db)):
    dado = CrudGenero(session).listar_generos()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.post("/",status_code=status.HTTP_201_CREATED)
def generos_usuario_gravar(lista: List[GeneroUsuarioCriar], session: Session = Depends(get_db)
                                    , current_user: User = Depends(obter_usuario_logado)
                                    ):
 
    if len(lista) < 3:
        raise HTTPException(status_code=404, detail='Deve haver um mínimo de 3 gêneros literários selecionados.')
    
    
    return CrudGenero(session).salvar_generos_usuario(lista, current_user.id)

@router.get("/usuarioGeneros", response_model=UsuarioGeneros)
async def listar_generos_usuario(session: Session = Depends(get_db)
, current_user: User = Depends(obter_usuario_logado)
):
    
    return CrudGenero(session).listar_generos_usuario(current_user.id)