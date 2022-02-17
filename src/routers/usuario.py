from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
import re

from src.core import hash_provider
from src.db.database import get_db
from src.crud.usuario import CrudUsuario
from src.schemas.usuario import Usuario, UsuarioCriar

router = APIRouter()

@router.get("/usuariostest")
async def dados_usuario(session: Session = Depends(get_db)):
    dado = CrudUsuario(session).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.get("/meusGeneros")
async def generos_usuario(session: Session = Depends(get_db)):
    dado = CrudUsuario(session).listar_generos()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.get("/gravarGeneros")
async def generos_usuario_gravar(generos_sele: Optional[List[int]] = Query(None), session: Session = Depends(get_db)):
    if not generos_sele or len(generos_sele) < 3:
        raise HTTPException(status_code=404, detail='Deve haver um mínimo de 3 gêneros literários selecionados.')
    
    dado = CrudUsuario(session).salvar_generos(generos_sele)
    return dado

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=Usuario)
def cadastrar(usuario: UsuarioCriar, session: Session = Depends(get_db)):
    #verifica campos vazios
    if not usuario.nome:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    if not usuario.apelido:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    if not usuario.senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Senha.")
    if not usuario.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o E-mail.")
    if not usuario.data_nascimento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Data de Nascimento.")


    #verifica senha
    """
    a expressão do regex diz:
    - senha deve ter de 8 a 20 digitos
    - espaços em branco não são permitidos
    """
    result_senha = re.match('^(?=\\S+$).{8,20}$', usuario.senha)
    if not result_senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A Senha deve conter no mínimo 8 dígitos e no máximo 20 dígitos.")

    #verifica se é maior de 18 anos
    idade = (date.today() - usuario.data_nascimento.date())
    result_idade = (idade.days / 365.25)
    if result_idade < 18.0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Você deve ser maior de idade para criar um conta.")

    #verifica se o apelido já está sendo utilizado
    apelido_buscado = CrudUsuario(session).buscar_por_apelido(usuario.apelido)
    if apelido_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse apelido.")
    #verifica se o email já está sendo utilizado
    email_buscado = CrudUsuario(session).buscar_por_email(usuario.email)
    if email_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")
    
    #

    #cria o novo usuário
    usuario.senha = hash_provider.get_password_hash(usuario.senha)
    usuario_criado = CrudUsuario(session).criar_usuario(usuario)
    return usuario_criado