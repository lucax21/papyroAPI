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
from src.schemas.user import UserSearch, UserUpdate, User, NewUser, BaseUser, UsersCompanyStatus, UsersCompany, Usuario, Suggestion
from src.utils.enum.reading_type import ReadingTypes

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_user(user: NewUser, session: Session = Depends(get_db)):
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


    email_buscado = CrudUser(session).get_by_email(user.email)
    if email_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")

    new_user = CrudUser(session).new_user(user)

    return 1


@router.get("/search"
, response_model=List[UserSearch]
)
def search_users(search: str, page: int = 0, session: Session = Depends(get_db)
,current_user: User = Depends(obter_usuario_logado)
):
    if not search:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo de pesquisa vazio.")

    return CrudUser(session).search_by_name(search, current_user.id, page)



@router.get("/viewProfile", response_model=Usuario)
async def view_profile(id: Optional[int] = None, session: Session = Depends(get_db),
                       current_user: User = Depends(obter_usuario_logado)):
    if not id:
        id = current_user.id
    return CrudUser(session).get_by_id(id)


@router.put("/editProfile", status_code=status.HTTP_200_OK)
async def editar_dados(usuario: UserUpdate, session: Session = Depends(get_db),
                       current_user: User = Depends(obter_usuario_logado)):
    usuario_db = CrudUser(session).get_user(current_user.id)

    return CrudUser(session).update_user(current_user.id, usuario)
    

@router.put("/atualizarFoto", status_code=status.HTTP_200_OK)
def atualizar_foto(link: str, session: Session = Depends(get_db)
                   , current_user: User = Depends(obter_usuario_logado)
                   ):
    return CrudUser(session).atualizar_foto(current_user.id, link)


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


@router.get("/{id}/company", response_model=UsersCompany)
async def get_company(id: int, session: Session = Depends(get_db)):
    return CrudUser(session).get_company(id)


@router.get("/{id_book}/{id_status}", response_model=UsersCompanyStatus)
async def book_user_status(
        id_book: int,
        id_status: int,
        session: Session = Depends(get_db)):
    if id_status != ReadingTypes.READING and id_status != ReadingTypes.READ and id_status != ReadingTypes.TO_READ:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Status do livro inválido.")

    return CrudUser(session).get_company_status(id_book, id_status)



@router.get("/extras/suggestion/get", response_model=Suggestion)
async def get_suggestion(current_user: User = Depends(obter_usuario_logado), page: Optional[int] = 0,
                      session: Session = Depends(get_db)):
    return CrudUser(session).get_suggestions(current_user.id, page)
