from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.core import hash_provider, token_provider
from src.schemas.login import Login, LoginSucesso
from src.db.database import get_db
from src.crud.usuario import CrudUsuario 

router = APIRouter()


@router.post("/", response_model=LoginSucesso)
def login(login: Login, session: Session = Depends(get_db)):
    
    if not login.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Preencha o E-mail.")

    if not login.senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Preencha a Senha.")

    usuario = CrudUsuario(session).buscar_por_email(login.email)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuário não cadastrado.")
    
    senha_valida = hash_provider.verify_password(login.senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Senha inválida.")
    
    token = token_provider.create_acess_token({'sub': usuario.email})

    return LoginSucesso(usuario=usuario, access_token=token)
