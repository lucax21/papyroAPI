from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.infra.providers import hash_provider, token_provider
from src.schemas.auth import Login, LoginSucesso
from src.schemas.usuario import Usuario
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario 
from src.routers.auth_utils import obter_usuario_logado
from datetime import date
import re

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(usuario: Usuario, session: Session = Depends(get_db)):
    #verifica campos vazios
    if not usuario.nome:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo nome vazio.")
    if not usuario.apelido:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo apelido vazio.")
    if not usuario.senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo senha vazio.")
    if not usuario.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo email vazio.")

    #verifica se é maior de 18 anos
    idade = (date.today() - usuario.data_nascimento.date())
    result_idade = (idade.days / 365.25)
    if result_idade < 18.0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Você deve ser maior de idade para criar um conta.")
  
    #verifica senha
    """
    a expressão do regex diz:
    - senha deve ter de 8 a 20 digitos
    - espaços em branco não são permitidos
    """
    result_senha = re.match('^(?=\\S+$).{8,20}$', usuario.senha)
    if not result_senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A senha fraca. Tente outra senha.")

    #verifica se o apelido já está sendo utilizado
    apelido_buscado = RepositorioUsuario(session).buscar_por_apelido(usuario.apelido)
    if apelido_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse apelido.")
    #verifica se o email já está sendo utilizado
    email_buscado = RepositorioUsuario(session).buscar_por_email(usuario.email)
    if email_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")
    
    #cria o novo usuário
    usuario.senha = hash_provider.get_password_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar_usuario(usuario)
    return usuario_criado

@router.post("/token", response_model=LoginSucesso)
def login(login: Login, session: Session = Depends(get_db)):
    email = login.email
    senha = login.senha
    
    if not senha or email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Campos vazios.")

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