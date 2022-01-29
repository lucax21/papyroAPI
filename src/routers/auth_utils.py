
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider 
from jose import JWTError

oauth2_schema = OAuth2PasswordBearer(tokenUrl = 'token')

def obter_usuario_logado(token: str = Depends(oauth2_schema),
                        session: Session = Depends(get_db)):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido.")


    try:
        email = token_provider.check_acess_token(token)
    except JWTError:
        raise exception
    
    if not email:
        raise exception
    
    usuario = RepositorioUsuario(session).buscar_por_email(email)

    if not usuario:
        raise exception

    return usuario