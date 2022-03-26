from urllib import response
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.core import hash_provider, token_provider
from src.db.models.models import Usuario

from src.schemas.login import Login,LoginSucesso
from src.core.config import Settings
from src.db.database import get_db
from src.crud.usuario import CrudUsuario
from src.schemas.usuario import UsuarioSimples 

settings = Settings()
router = APIRouter()


@router.post("/", response_model=LoginSucesso)
def login(login: Login, session: Session = Depends(get_db)):
    
    if not login.email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Preencha o E-mail.")
    elif not login.senha:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Preencha a Senha.")


    usuario = CrudUsuario(session).buscar_por_email(login.email)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Usuário não cadastrado.")
    
    if usuario.ativo == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Por favor, ative sua conta.")

    senha_valida = hash_provider.verify_password(login.senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Senha inválida.")
    
    access_token = token_provider.create_acess_token({'sub': usuario.email},
                                            expires_delta=settings.USER_TOKEN_LIFETIME )
    
    us = UsuarioSimples()
    us.nome=usuario.nome
    us.apelido=usuario.apelido
    us.foto=usuario.foto
    us.descricao=usuario.descricao
    lo = LoginSucesso()
    lo.usuario=us
    lo.access_token=access_token
    lo.token_type="Bearer"
    # return {"usuario": usuario, "access_token": access_token, "token_type": "Bearer"}
    return lo