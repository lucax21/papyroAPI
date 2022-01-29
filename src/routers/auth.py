from urllib import response
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import LoginSucesso
from src.infra.providers import hash_provider, token_provider
from src.schemas.schemas import Usuario, Login
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario 
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    #verifica se é maior de 18 anos
    
    #verifica se o email já está sendo utilizado
    usuario_buscado = RepositorioUsuario(session).buscar_por_email(usuario.email)
    if usuario_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")
    
    #cria o novo usuário
    usuario.senha = hash_provider.get_password_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar_usuario(usuario)
    return usuario_criado

@router.post("/token", response_model=LoginSucesso)
def login(login: Login, session: Session = Depends(get_db)):
    email = login.email
    senha = login.senha
    
    usuario = RepositorioUsuario(session).buscar_por_email(email)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email inválido.")
    
    senha_valida = hash_provider.verify_password(senha, usuario.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Senha inválida.")
    
    token = token_provider.create_acess_token({'sub': usuario.email})

    return LoginSucesso(usuario=usuario, access_token=token)

@router.get("/me")
def me(usuario: Usuario = Depends(obter_usuario_logado)):
    return usuario