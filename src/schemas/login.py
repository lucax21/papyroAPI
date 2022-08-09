from typing import Optional

from pydantic import BaseModel, EmailStr

from src.schemas.user import BaseUser


class Login(BaseModel):
    password: str
    email: EmailStr


class LoginSucesso(BaseModel):
    user: Optional[BaseUser] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    token_type: Optional[str] = None
