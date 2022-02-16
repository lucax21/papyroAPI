from sys import prefix
from fastapi import APIRouter
from src.routers import usuario, auth, genero

router = APIRouter()

router.include_router(auth.router, prefix="/auth")
router.include_router(usuario.router, prefix="/usuario")
router.include_router(genero.router, prefix="/genero")
