from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.crud.comment import CrudComment
from src.db.database import get_db
# from src.schemas.comment import SaveComment
from src.routers.login_utils import obter_usuario_logado
from src.schemas.comment import Comments
from src.schemas.usuario import Usuario

router = APIRouter()


# @router.post("/")
# def save_comment(dado: SaveComment, session: Session = Depends(get_db)):
#     if not dado.texto:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insira uma Mensagem para enviar.")
#     return CrudComentario(session).salvar_comentario(24, dado)

@router.get("/{rate_id}", response_model=Comments)
async def get_comments(rate_id: int,
                       page: int = 0,
                       current_user: Usuario = Depends(obter_usuario_logado),
                       session: Session = Depends(get_db)):
    return CrudComment(session).get_comments(rate_id, current_user.id, page)
