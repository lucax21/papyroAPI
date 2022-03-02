from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.core import hash_provider, token_provider

from src.schemas.login import Login
from src.core.config import Settings
from src.db.database import get_db
from src.crud.usuario import CrudUsuario 

settings = Settings()
router = APIRouter()


@router.post("/")
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
                    detail="Please, activate your Account")

    senha_valida = hash_provider.verify_password(login.senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Senha inválida.")
    
    access_token = token_provider.create_acess_token({'sub': usuario.email},
                                            expires_delta=settings.USER_TOKEN_LIFETIME )

    return {"access_token": access_token, "token_type": "Bearer"}
