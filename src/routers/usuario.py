from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.schemas import schemas
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

router = APIRouter()

@router.get("/usuarios_test")
async def dados_usuario(db: Session = Depends(get_db)):
    dado = RepositorioUsuario(db).listar()
    return dado

@router.post("/usuario", status_code=status.HTTP_201_CREATED)
async def criar_usuario(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar_usuario(usuario)
    return usuario_criado
