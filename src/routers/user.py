from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from src.crud.login import CrudLogin
from src.crud.user import CrudUser
from src.db.database import get_db
from src.utils.login_utils import obter_usuario_logado
from src.schemas.user import UserSearch, UserUpdate, User, NewUser, Usuario, Suggestion

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def new_user(user: NewUser, session: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
    if not user.name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Nome.")
    elif not user.nickname:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o seu Apelido.")
    elif not user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha a Senha.")
    elif not user.email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Preencha o E-mail.")

    email_buscado = CrudUser(session).get_by_email(user.email)
    if email_buscado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Já existe um usuário com esse email.")

    new_user = CrudUser(session).new_user(user)

    return CrudLogin(session, Authorize).login(new_user, user.password)


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
    return CrudUser(session).get_by_id(id, current_user.id)


@router.put("/editProfile", status_code=status.HTTP_200_OK)
async def edit_profile(data: UserUpdate, session: Session = Depends(get_db),
                       current_user: User = Depends(obter_usuario_logado)):

    return CrudUser(session).update_user(current_user.id, data)
    

@router.put("/updatePhoto", status_code=status.HTTP_200_OK)
def update_photo(link: str, session: Session = Depends(get_db)
                   , current_user: User = Depends(obter_usuario_logado)
                   ):
    return CrudUser(session).update_photo(current_user.id, link)


@router.get("/extras/suggestion/get", response_model=Suggestion)
async def get_suggestion(current_user: User = Depends(obter_usuario_logado), page: Optional[int] = 0,
                      session: Session = Depends(get_db)):
    return CrudUser(session).get_suggestions(current_user.id, page)
