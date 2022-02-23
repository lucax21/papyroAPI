from jose import jwt
from datetime import datetime, timedelta
from pydantic import UUID4

from src.core.config import Settings

settings = Settings()


@staticmethod
def create_acess_token(data: dict, expires_delta: int):
    to_encode = data.copy()
    
    to_encode.update({
            "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
            "iss": settings.PROJECT_NAME
        })
    
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM)

@staticmethod
def check_acess_token(token: str):
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
    return payload.get('sub')

@staticmethod
def get_confirmation_token(user_email: str, jti: UUID4):
    claims = {
        "sub": str(user_email),
            "scope": "registration",
            "jti": str(jti)
        }
    return {
            "jti": str(jti),
            "token": create_acess_token(
                claims,
                settings.REGISTRATION_TOKEN_LIFETIME
            )
        }