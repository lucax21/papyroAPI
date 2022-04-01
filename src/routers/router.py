from sys import prefix
from fastapi import APIRouter

from src.routers import login, usuario, genero, grupo, livro, avaliacao, comentario

router = APIRouter()

router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(usuario.router, prefix="/usuarios", tags=["usuarios"])
router.include_router(genero.router, prefix="/generos", tags=["generos"])
router.include_router(livro.router, prefix="/livros", tags=["livros"])
router.include_router(grupo.router, prefix="/grupos", tags=["grupos"])
router.include_router(avaliacao.router, prefix="/avaliacoes", tags=["avaliacoes"])
router.include_router(comentario.router, prefix="/comentarios", tags=["comentarios"])