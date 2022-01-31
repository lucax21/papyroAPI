from pydantic import BaseModel

from src.schemas.usuario import UsuarioSimples

class Login(BaseModel):
    senha: str
    email: str

class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str