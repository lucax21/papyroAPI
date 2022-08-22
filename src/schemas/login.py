from typing import Optional

from pydantic import BaseModel, EmailStr, validator
from fastapi import HTTPException, status
from src.schemas.user import BaseUser
import re

class Login(BaseModel):
    password: str
    email: EmailStr

class LoginSucesso(BaseModel):
    user: Optional[BaseUser] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    token_type: Optional[str] = None

class ResetPassword(BaseModel):
    reset_password_token: str
    new_password: str
    confirm_password: str

    @validator('new_password')
    def vl_password(cls, value):
        password = re.match('^(?=\\S+$).{8,32}$', value)
        if not password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A senha deve conter no mínimo 8 dígitos e no máximo 32 dígitos.")
        return value
    
    @validator('confirm_password')
    def vl_confirm_password(cls,v , values, **kwargs):
        if 'password' in values and v != values['new_password']:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A senhas são diferentes.")
        

class ForgotPassword(BaseModel):
    email: EmailStr
