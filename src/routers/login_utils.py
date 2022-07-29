from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from src.crud.usuario import CrudUsuario
from src.db.database import get_db
from src.core import token_provider 

from src.core.config import Settings
from jose import JWTError

settings = Settings()
oauth2_schema = OAuth2PasswordBearer(tokenUrl = 'token')

def obter_usuario_logado(token: str = Depends(oauth2_schema),
                        session: Session = Depends(get_db)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido.")

    try:
        username = token_provider.check_access_token(token)

        if username is None:
            raise exception
    
    except JWTError:
        raise exception
    
    user = CrudUsuario(session).current_user(username)

    if user is None:
        raise exception
    
    return user