from src.utils import hash_provider
from src.utils.config import settings
from src.crud.user import CrudUser
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from src.schemas.login import LoginSucesso
from src.schemas.user import BaseUser


class CrudLogin:
    def __init__(self, session: Session, Authorize):
        self.session = session
        self.Authorize = Authorize

    def login(self, login, password=None):
        user = CrudUser(self.session).get_by_email(login.email)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Email ou senha inválida.")

        senha_valida = hash_provider.verify_password(password if password else login.password, user.password)
        if not senha_valida:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Email ou senha inválida.")

        access_token = self.Authorize.create_access_token(subject=user.email, expires_time=settings.USER_TOKEN_LIFETIME)
        refresh_token = self.Authorize.create_refresh_token(subject=user.email, expires_time=None)

        us = BaseUser()
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