
import email
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Propriedades compartilhadas
class UsuarioSimples(BaseModel):
    nome: str
    apelido: str
    email: Optional[EmailStr] = None
    data_nascimento: datetime
    foto: Optional[str] = None

# Propriedades a receber via API na criação
class UsuarioCriar(UsuarioSimples):
    email: EmailStr
    senha: str

class UsuarioDb(UsuarioSimples):
    id: Optional[int] = None

class Usuario(UsuarioDb):
    pass