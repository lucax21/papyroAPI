from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.crud.comment import CrudComment
from src.db.database import get_db
from src.routers.login_utils import obter_usuario_logado
from src.schemas.comment import Comments, NewComment, CommentReturn
from src.schemas.user import User

router = APIRouter()


@router.post("/", response_model=CommentReturn)
def comment(data: NewComment,
            current_user: User = Depends(obter_usuario_logado),
            session: Session = Depends(get_db)):

    if not data.text or len(data.text) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Comentário muito curto.")

    return CrudComment(session).new_comment(data, current_user.id)


@router.get("/{rate_id}", response_model=Comments)
async def get_comments(rate_id: int,
                       page: int = 0,
                       current_user: User = Depends(obter_usuario_logado),
                       session: Session = Depends(get_db)):

    return CrudComment(session).get_comments(rate_id, current_user.id, page)
