from fastapi import APIRouter, Depends, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session
from src.core.email_provider import Mailer
from src.core import hash_provider
from src.core.config import Settings
from src.crud.user import CrudUser
from src.db.database import get_db
from src.schemas.login import ResetPassword, ForgotPassword, Login, LoginSucesso
from src.schemas.user import BaseUser
from src.core.token_provider import check_access_token, get_confirmation_token
import uuid

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

    user = CrudUser(session).get_by_email(login.email)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Usuário não cadastrado.")

    senha_valida = hash_provider.verify_password(login.password, user.password)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Senha inválida.")

    access_token = Authorize.create_access_token(subject=user.email, expires_time=settings.USER_TOKEN_LIFETIME)
    refresh_token = Authorize.create_refresh_token(subject=user.email, expires_time=None)

    us = BaseUser()
    us.name = user.name
    us.nickname = user.nickname
    us.photo = user.photo
    us.description = user.description
    us.birthday = user.formatted_birthday

    lo = LoginSucesso()
    lo.user = us
    lo.access_token = access_token
    lo.refresh_token = refresh_token
    lo.token_type = "Bearer"
    return lo


@router.get("/refresh")
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}

@router.get("/verification")
def verification(token: str, session: Session = Depends(get_db)):
    invalid_token_error = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Token.')

    try:
        payload = check_access_token(token)
    except jwt.JWSError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token has expired")
    user = CrudUser(session).get_verification(email=payload)

    if user.active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already activated")
    
    CrudUser(session).active_account(user.id, None, True)

    return 1

@router.patch("/resetPassword")
async def reset_password(request: ResetPassword, session: Session = Depends(get_db)):
    
    reset_token = CrudUser(session).check_reset_password_token(request.reset_password_token)
    

    CrudUser(session).reset_password(reset_token.email, request.new_password)


    
    return 1


@router.post("/forgotPassword")
async def forgot_password(user: ForgotPassword, session: Session = Depends(get_db)):
    result = CrudUser(session).get_by_email(user.email)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_BAD_REQUEST, detail="Error. Not found.")
    
    reset_code = str(uuid.uuid1())

    CrudUser(session).reset_code(result.email, reset_code)

    Mailer.forgot_password(reset_code, result.email)

    return 1
