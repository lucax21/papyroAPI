from pydantic import BaseModel
from typing import Optional

from src.schemas.usuario import UsuarioSimples

class Login(BaseModel):
    password: str
    email: str

class LoginSucesso(BaseModel):
    user: Optional[UsuarioSimples] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    token_type: Optional[str] = None
