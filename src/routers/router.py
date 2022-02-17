from fastapi import APIRouter

from src.routers import login, usuario, genero

router = APIRouter()

router.include_router(login.router, prefix="/login", tags=["login"])
router.include_router(usuario.router, prefix="/usuarios", tags=["usuarios"])
router.include_router(genero.router, prefix="/generos", tags=["generos"])
