from fastapi import APIRouter, Depends, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session

from src.core import hash_provider
from src.core.config import Settings
from src.crud.usuario import CrudUsuario
from src.db.database import get_db
from src.schemas.login import Login, LoginSucesso
from src.schemas.usuario import UsuarioSimples

settings = Settings()
router = APIRouter()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post("/", response_model=LoginSucesso)
def login(login: Login, session: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    if not login.email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Preencha o E-mail.")
    elif not login.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Preencha a Senha.")

    user = CrudUsuario(session).buscar_por_email(login.email)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Usuário não cadastrado.")

    if not user.active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Por favor, ative sua conta.")

    senha_valida = hash_provider.verify_password(login.password, user.password)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Senha inválida.")

    access_token = Authorize.create_access_token(subject=user.email, expires_time=settings.USER_TOKEN_LIFETIME)
    refresh_token = Authorize.create_refresh_token(subject=user.email, expires_time=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    us = UsuarioSimples()
    us.name = user.name
    us.nickname = user.nickname
    us.photo = user.photo
    us.description = user.description

    lo = LoginSucesso()
    lo.user = us
    lo.access_token = access_token
    lo.refresh_token = refresh_token
    lo.token_type = "Bearer"
    return lo


@router.post("/refresh")
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}
