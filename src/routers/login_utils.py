from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
import math, random

from src.core import token_provider
from src.core.config import Settings
from src.crud.user import CrudUser
from src.db.database import get_db

settings = Settings()
oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def obter_usuario_logado(token: str = Depends(oauth2_schema),
                         session: Session = Depends(get_db)):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido.")

    try:
        username = token_provider.check_access_token(token)

        if not username:
            raise exception

    except JWTError:
        raise exception

    user = CrudUser(session).current_user(username)

    if not user:
        raise exception

    return user


def generateOTP():
    #uma opção mais forte
   # string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    string = '0123456789abcdefghijklmnopqrstuvwxyz'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]
 
    return OTP