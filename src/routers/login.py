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
import math, random


settings = Settings()
router = APIRouter()


@AuthJWT.load_config
def get_config():
    return Settings()


def generateOTP():
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
 
    return OTP


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


@router.post("/resetPassword")
def reset_password(data: ResetPassword, session: Session = Depends(get_db)):
    reset_code = CrudUser(session).check_reset_password_code(data.reset_password_code, data.email)

    if not reset_code:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Código expirado.")

    CrudUser(session).reset_password(data.email, data.new_password)

    return 1


@router.post("/forgotPassword")
async def forgot_password(user: ForgotPassword, session: Session = Depends(get_db)):
    result = CrudUser(session).get_by_email(user.email)
    if not result:
        return 1
    
    code_otp = generateOTP()

    CrudUser(session).save_reset_code(result.email, code_otp)

    Mailer.forgot_password(code_otp, result.email)

    return 1
