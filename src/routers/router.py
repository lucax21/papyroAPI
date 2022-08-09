from fastapi import APIRouter

from src.routers import genero, login, usuario, book, avaliacao, comment, mensagem, like, feed

router = APIRouter()

router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(usuario.router, prefix="/users", tags=["users"])
router.include_router(genero.router, prefix="/genres", tags=["genres"])
router.include_router(book.router, prefix="/getBook", tags=["books"])
router.include_router(avaliacao.router, prefix="/avaliacoes", tags=["avaliacoes"])
router.include_router(comment.router, prefix="/comments", tags=["comments"])
router.include_router(mensagem.router, prefix="/mensagens", tags=["mensagens"])
router.include_router(like.router, prefix="/like", tags=["likes"])
router.include_router(feed.router, prefix="/feed", tags=["feed"])
