from fastapi import APIRouter
from src.routers import usuario

router = APIRouter()

router.include_router(usuario.router)