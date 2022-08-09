import re
from datetime import date, datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.core.email_provider import Mailer
from src.core.token_provider import get_confirmation_token
from src.crud.user import CrudUser
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.book import BookByType
from src.schemas.user import UserUpdate, User, UserAddBookToLibrary, UserNew, BaseUser
from src.utils.enum.reading_type import ReadingTypes

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
async def cadastrar(user: UserNew, session: Session = Depends(get_db)):
    # verifica campos vazios
    if not user.name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    elif not user.nickname:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    elif not user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Senha.")
    elif not user.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o E-mail.")
    elif not user.birthday:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Data de Nascimento.")

    # verifica senha
    """
    a expressão do regex diz:
    - senha deve ter de 8 a 20 digitos
    - espaços em branco não são permitidos
    """
    result_senha = re.match('^(?=\\S+$).{8,20}$', user.password)
    if not result_senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="A Senha deve conter no mínimo 8 dígitos e no máximo 20 dígitos.")

    # verifica se é maior de 18 anos
    idade = (date.today() - datetime.strptime(user.birthday, '%Y-%m-%d'))
    result_idade = (idade.days / 365.25)
    if result_idade < 18.0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Você deve ser maior de idade para criar um conta.")

    # verifica se o apelido já está sendo utilizado
    apelido_buscado = CrudUser(session).buscar_por_apelido(user.nickname)
    if apelido_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse apelido.")
    # verifica se o email já está sendo utilizado
    email_buscado = CrudUser(session).get_by_email(user.email)
    if email_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")

    # cria o novo usuário
    usuario_criado = CrudUser(session).new_user(user)

    token_confirmacao = get_confirmation_token(usuario_criado.email, usuario_criado.confirmacao)

    try:
        Mailer.enviar_email_confirmacao(token_confirmacao["token"], usuario_criado.email)
    except ConnectionRefusedError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Email não poderia ser enviado. Por favor, tente de novo."
        )

    return usuario_criado


@router.get("/conversas", response_model=User)
def conversas(session: Session = Depends(get_db)
              , current_user: User = Depends(obter_usuario_logado)):
    pass


@router.get("/buscarUsuarios{termo}", response_model=List[User])
def buscar_usuario(termo: str, session: Session = Depends(get_db)):
    if not termo:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudUser(session).search_by_name(termo)
    if not dado:
        raise HTTPException(status_code=404, detail='Não encontrado')
    return dado


@router.get("/get/{id}", response_model=User)
def buscar_por_id(id: int, session: Session = Depends(get_db)):
    if not id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Termo de pesquisa vazio.")

    dado = CrudUser(session).get_by_id(id)
    if not dado:
        CrudUser(session).perfil_usuario(id)
    return dado


@router.get("/viewProfile/{id}", response_model=User)
async def view_profile(id: Optional[int], session: Session = Depends(get_db),
                       current_user: User = Depends(obter_usuario_logado)):
    if not id:
        id = current_user.id
    return CrudUser(session).get_by_id(id)


@router.put("/atualizarDados", status_code=status.HTTP_200_OK)
async def editar_dados(usuario: UserUpdate, session: Session = Depends(get_db),
                       current_user: User = Depends(obter_usuario_logado)):
    # verifica campos vazios
    # if not usuario.name:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    # elif not usuario.nickname:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    # elif not usuario.birthday:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Data de Nascimento.")

    # verifica se o usuário vai trocar de nickname
    usuario_db = CrudUser(session).get_user(current_user.id)
    if not usuario_db['nickname'] == usuario.nickname:
        # verifica se o apelido já está sendo utilizado
        apelido_buscado = CrudUser(session).buscar_por_apelido(usuario.nickname)
        if apelido_buscado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse apelido.")

    CrudUser(session).atualizar_usuario(current_user.id, usuario)
    # return usuario_db['nickname']


@router.get("/editProfile", response_model=BaseUser)
async def edit_profile(session: Session = Depends(get_db)
                       , current_user: User = Depends(obter_usuario_logado)):
    return CrudUser(session).get_user(current_user.id)


@router.put("/atualizarFoto", status_code=status.HTTP_200_OK)
def atualizar_foto(link: str, session: Session = Depends(get_db)
                   , current_user: User = Depends(obter_usuario_logado)
                   ):
    CrudUser(session).atualizar_foto(current_user.id, link)
    # return link


@router.get("/books/{reading_type}", response_model=List[BookByType])
def get_user_books(reading_type: str,
                   user_id: Optional[int] = None,
                   page: int = 0,
                   current_user: User = Depends(obter_usuario_logado),
                   session: Session = Depends(get_db)):
    if not user_id:
        user_id = current_user.id

    if reading_type == 'reading':
        return CrudUser(session).user_books(user_id, ReadingTypes.READING, page)
    if reading_type == 'read':
        return CrudUser(session).user_books(user_id, ReadingTypes.READ, page)
    if reading_type == 'to_read':
        return CrudUser(session).user_books(user_id, ReadingTypes.TO_READ, page)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passe o parâmetro de leitura.")


@router.post("/addLivroBiblioteca/")
def add_livro_biblioteca(addLivro: UserAddBookToLibrary, session: Session = Depends(get_db)
                         , current_user: User = Depends(obter_usuario_logado)
                         ):
    pass
    # return CrudUsuario(session).add_livro_biblioteca(current_user.id, addLivro)
