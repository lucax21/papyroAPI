from urllib import response
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from datetime import date
import re

from typing import List, Optional
from src.core.token_provider import check_acess_token, get_confirmation_token
from src.db.database import get_db
from src.db.models.models import Book
from src.routers.login_utils import obter_usuario_logado
from src.crud.usuario import CrudUsuario
from src.schemas.usuario import AtualizarFoto, Usuario, UsuarioAddLivroBiblioteca, UsuarioCriar, UsuarioPerfil
from src.schemas.livro import LivroId, LivroSimples
from jose import jwt

from src.core.email_provider import Mailer


router = APIRouter()


@router.get("/usuariostest12"
# , response_model=List[Usuario]
)
async def dados_usuario(session: Session = Depends(get_db)):
    dado = CrudUsuario(session).listar()
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=Usuario)
async def cadastrar(usuario: UsuarioCriar, session: Session = Depends(get_db)):
    #verifica campos vazios
    if not usuario.nome:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    elif not usuario.apelido:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    elif not usuario.senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Senha.")
    elif not usuario.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o E-mail.")
    elif not usuario.data_nascimento:
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
    idade = (date.today() - usuario.data_nascimento)
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
    
 
    #cria o novo usuário
    usuario_criado = CrudUsuario(session).criar_usuario(usuario)

    token_confirmacao = get_confirmation_token(usuario_criado.email, usuario_criado.confirmacao)

    try:
        Mailer.enviar_email_confirmacao(token_confirmacao["token"], usuario_criado.email)
    except ConnectionRefusedError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Email não poderia ser enviado. Por favor, tente de novo."
        )

    return usuario_criado

@router.get("/verificacao/{token}",status_code=status.HTTP_201_CREATED, response_model=Usuario)
def verificar(token: str, session: Session = Depends(get_db)):
    invalid_token_error = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Token")

    # Trying decode token
    try:
        payload = check_acess_token(token)
        # print("##############")
        # print(payload)
        # # print(payload['scope'])
        # print("#############33")
    except jwt.JWSError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Token has Expired")


    #check if the scope is ok
    # if payload['scope'] != 'registration':
    #     raise invalid_token_error
    
    # try to get an user with the id from token
    # user = CrudUsuario(session).buscar_por_email(email=payload['sub'])
    user = CrudUsuario(session).buscar_por_email(email=payload)

    # check if we found an user and if the uid confirmation is the same of the token
    # if not user or (user.confirmacao) != payload['jti']:
    #     raise invalid_token_error
    
    #check if the user is already active
    if user.ativo:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="User already Activated")
    
    # if all it's ok, we update the confirmation and 'ativo' attribute and call the save
    user.confirmacao = None
    user.ativo = True
    CrudUsuario(session).ativar_conta(user)

    return user

@router.get("/conversas", response_model=Usuario)
def conversas(session: Session = Depends(get_db)
            , current_user: Usuario = Depends(obter_usuario_logado)):
    pass

@router.get("/buscarUsuarios{termo}",response_model=List[Usuario])
def buscar_usuario(termo: str,session: Session = Depends(get_db)):
    if not termo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudUsuario(session).buscar_por_nome(termo)
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado

@router.get("/get/{id}",response_model=Usuario)
def buscar_por_id(id: int,session: Session = Depends(get_db)):
    if not id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudUsuario(session).buscar_por_id(id)
    if not dado:
        CrudUsuario(session).perfil_usuario(id)
    return dado

@router.get("/meusDados",response_model=Usuario)
def dados_usuarios(session: Session = Depends(get_db),current_user: Usuario = Depends(obter_usuario_logado)):  
    return CrudUsuario(session).buscar_por_id(current_user.id)

@router.get("/visualizarPerfil/{id}"
# , response_model=UsuarioPerfil
)
def dados_perfil(id:Optional[int], session: Session = Depends(get_db),current_user: Usuario = Depends(obter_usuario_logado)):  
    
    try:
        if id:
            dado = CrudUsuario(session).perfil_usuario(id)
        else:
            dado = CrudUsuario(session).perfil_usuario(current_user.id)
        
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")
    return dado


@router.put("/atualizarDados")
def editar_dados(usuario: UsuarioCriar, session: Session = Depends(get_db), current_user: Usuario = Depends(obter_usuario_logado)):
    #verifica campos vazios
    if not usuario.nome:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    elif not usuario.apelido:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    elif not usuario.data_nascimento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Data de Nascimento.")

    #verifica se é maior de 18 anos
    idade = (date.today() - usuario.data_nascimento)
    result_idade = (idade.days / 365.25)
    if result_idade < 18.0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Você deve ser maior de idade para criar um conta.")

    usuario_db = CrudUsuario(session).buscar_por_id(current_user.id)

    if not usuario.apelido == usuario_db.apelido:     
        #verifica se o apelido já está sendo utilizado
        apelido_buscado = CrudUsuario(session).buscar_por_apelido(usuario.apelido)
        if apelido_buscado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse apelido.")

   
    return CrudUsuario(session).atualizar_usuario(current_user.id, usuario)

@router.post("/atualizarFoto")
def atualizar_foto(link: AtualizarFoto,session: Session = Depends(get_db)
,current_user: Usuario = Depends(obter_usuario_logado)
):

    return CrudUsuario(session).atualizar_foto(current_user.id,link)

@router.get("/{id}/livrosSeraoLidos/"
# , response_model=List[Livro]
)
def livros_lerei(id: int, session: Session = Depends(get_db)
,current_user: Usuario = Depends(obter_usuario_logado)
):
    return CrudUsuario(session).livros_serao_lidos(id)

@router.get("/{id}/livrosLidos/"
# , response_model=List[LivroSimples]
)
def livros_lidos(id: int, session: Session = Depends(get_db)
,current_user: Usuario = Depends(obter_usuario_logado)
):
    return CrudUsuario(session).livros_lidos(id)

@router.get("/{id}/livrosLendo/"
# , response_model=List[LivroSimples]
)
def livros_lendo(id: int, session: Session = Depends(get_db)
,current_user: Usuario = Depends(obter_usuario_logado)
):
    return CrudUsuario(session).livros_lendo(id)

@router.post("/addLivroBiblioteca/")
def add_livro_biblioteca(addLivro: UsuarioAddLivroBiblioteca,session: Session = Depends(get_db)
,current_user: Usuario = Depends(obter_usuario_logado)
):
    return CrudUsuario(session).add_livro_biblioteca(current_user.id, addLivro)