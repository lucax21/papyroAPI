from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.core import hash_provider, token_provider
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.login import Login,LoginSucesso
from src.core.config import Settings
from src.db.models.models import User
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.crud.usuario import CrudUsuario
from src.schemas.usuario import UsuarioSimples 

settings = Settings()
router = APIRouter()


@router.post("/"
, response_model=LoginSucesso
)
def login(login: Login, session: Session = Depends(get_db)):
	try:
		if not login.email:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
								detail="Preencha o E-mail.")
		elif not login.password:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
								detail="Preencha a Senha.")


		user = CrudUsuario(session).buscar_por_email(login.email)
		
		if not user:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
								detail="Usuário não cadastrado.")
		
		if user.active == False:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
						detail="Por favor, ative sua conta.")

		senha_valida = hash_provider.verify_password(login.password, user.password)

		if not senha_valida:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
								detail="Senha inválida.")
		
		access_token = token_provider.create_access_token({'sub': user.email},
												expires_delta=settings.USER_TOKEN_LIFETIME )
		
		refresh_token = token_provider.create_refresh_token({'sub': user.email}, expires_delta=settings.REFRESH_TOKEN_EXPIRE_MINUTES)

		us = UsuarioSimples()
		us.name=user.name
		us.nickname=user.nickname
		us.photo=user.photo
		us.description=user.description
		
		lo = LoginSucesso()
		lo.user=us
		lo.access_token=access_token
		lo.refresh_token=refresh_token
		lo.token_type="Bearer"
		return lo
	except:
		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
	

@router.post("/refresh")
def refresh(current_user: User = Depends(obter_usuario_logado)):
	
	new_access_token = token_provider.create_access_token({'sub': current_user.email},
												expires_delta=settings.USER_TOKEN_LIFETIME)
	
	return {"access_token": new_access_token, "token_type":"Bearer"}