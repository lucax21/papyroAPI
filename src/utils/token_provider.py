from http.client import HTTPException
from jose import jwt
from datetime import datetime, timedelta
from pydantic import UUID4, ValidationError
from fastapi import HTTPException, status

from src.utils.config import Settings

settings = Settings()


def create_access_token(data: dict, expires_delta: int = None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.USER_TOKEN_LIFETIME)

    to_encode = data.copy()
    
    to_encode.update({
            "exp": expires_delta,
            "iss": settings.PROJECT_NAME
        })
    
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM)


def check_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
    except(jwt.JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"},)
    
    return payload.get("sub")


def get_confirmation_token(user_email: str, jti: UUID4):
    claims = {
        "sub": str(user_email),
            "scope": "registration",
            "jti": str(jti)
        }
    return {
            "jti": str(jti),
            "token": create_access_token(
                claims,
                settings.REGISTRATION_TOKEN_LIFETIME
            )
        }


def create_refresh_token(data: dict, expires_delta: int = None):
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = data.copy()
    
    to_encode.update({
            "exp": expires_delta,
            "iss": settings.PROJECT_NAME
        })
    
    return jwt.encode(to_encode, settings.REFRESH_SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM)
