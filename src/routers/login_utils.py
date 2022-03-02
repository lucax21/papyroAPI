
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from src.crud.usuario import CrudUsuario
from src.db.database import get_db
from src.core import token_provider 

from src.core.config import Settings
from jose import JWTError,jwt

settings = Settings()
oauth2_schema = OAuth2PasswordBearer(tokenUrl = 'token')

def obter_usuario_logado(token: str = Depends(oauth2_schema),
                        session: Session = Depends(get_db)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido.")


    try:
        # payload = token_provider.check_acess_token(token)
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
        username: str = payload.get("sub")
        # print("username is", username)

        if not username:
            raise exception
    
    except JWTError:
        raise exception
    
    if not payload:
        raise exception
    
    usuario = CrudUsuario(session).buscar_por_email(username)

    if not usuario:
        raise exception

    return usuario