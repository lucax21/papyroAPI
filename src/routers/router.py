from fastapi import APIRouter
from src.routers import usuario, auth

router = APIRouter()

router.include_router(auth.router, prefix="/auth")

router.include_router(usuario.router, prefix="/usuario")

