from fastapi import APIRouter

from src.routers import login, usuario, genero, book, avaliacao, comment, mensagem

router = APIRouter()

router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(usuario.router, prefix="/users", tags=["users"])
router.include_router(genero.router, prefix="/generos", tags=["generos"])
router.include_router(book.router, prefix="/getBook", tags=["books"])
router.include_router(avaliacao.router, prefix="/avaliacoes", tags=["avaliacoes"])
router.include_router(comment.router, prefix="/comments", tags=["comments"])
router.include_router(mensagem.router, prefix="/mensagens", tags=["mensagens"])
